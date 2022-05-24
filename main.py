import serial
import time
from nesp_lib import Port, Pump, PumpingDirection
import functions
import Operations

import site


#Config for the valve Hamilton serial MVP
NbofValve=1                                                                     # Nb of valve in series
PortValve='COM8'                                                          # Communication port of the first valve
ValveNB=("a")       # List wich contains all the adress possible 
ValveConfigPosition={};
ValveConfigPosition["a"]=8                                                      # Configuration of the first valve
class Valve:
    def __init__(self):
        """
        For the class instanciation, the input variable port is indicating which
        COM port the valve is connected to.
        Parameters
        ----------
        None.
        Returns
        -------
        None.
        """
        self.port = PortValve  # Save the name of the port given in the "file Config.py" in "self.port"
        self.ValveState = {}  # Create a dictionnary

    def OpenConnection(self):
        """
        The OpenConnection method is opening the serial communication port and
        keeps the output in self.
        The time delay of 2s is important to keep, else the communication will
        not be established and it won't be possible to control the valve.
        Returns
        -------
        None.
        """
        try:
            self.s = serial.Serial(self.port, baudrate=9600, bytesize=serial.SEVENBITS, parity=serial.PARITY_ODD,
                                   stopbits=serial.STOPBITS_ONE)  # Open the port and keep the output in self.s
            time.sleep(2)  # Wait 2 seconds
            self.s.flushInput()  # Remove data from input buffer
            Init = "1a\r"  # This str input ask the device to do an auto adressing (First valve="a"; Second valve="b"; ....)
            self.s.write(Init.encode())  # Send the command to the device encoded in UTF-8
            for i in range(0, NbofValve):  # We want to initialize every valve adressed
                string2Send = ValveNB[
                                  i] + "LXR\r"  # This str input initialize the current valve (ValveNB[0]='a';ValveNB[1]='b')
                self.s.write(string2Send.encode())  # Send the command to the device encoded in UTF-8
                Valve.WaitForIdle(
                    self)  # Use the method WaitForIdle to be sure the initialization is finished before sending new instructions
                self.ValveState["ValvePosition" + str(ValveNB[
                                                          i])] = 1  # Save the position of each valve (After initialization every valve shall be in position 1)
                self.ValveState["Outrange" + str(
                    ValveNB[i])] = "Values within limits"  # For now all the values are in the limits
        except AttributeError:
            print("The port " + str(self.port) + "is already opened")
        except serial.SerialException:
            print("Wrong port given, please check the file Config.py")

    def Status(self):
        """
        The Status method is checking if the one of the valve is doing something or not
        Returns
        -------
        None.
        """
        self.s.flushInput()  # Remove data from input buffer
        for i in range(0, NbofValve):  # Check the state of each valve
            self.s.flushInput()  # Remove data from input buffer
            status = ValveNB[i] + "F\r"  # This str input ask to the current valve his state
            self.s.write(status.encode())  # Send the command to the device encoded in UTF-8
            Line1 = self.s.read()  # First line give us useless information so we will not use it
            Output = self.s.read()  # Return "*" if the valve is busy "Y" if the valve is idle
            self.ValveState[
                "State" + ValveNB[i]] = Output.decode()  # Save the state of the current valve in the dictionnary

    def WaitForIdle(self):
        """
        The WaitForIdle method wait 1 sec if one of the valve is already working
        Returns
        -------
        None.
        """
        Valve.Status(self)  # Check the status of each valve
        WaitingTime = 0
        for i in range(0, NbofValve):  # Check if the status is idle or not for each device
            while self.ValveState["State" + ValveNB[
                i]] != "Y":  # While the status is not "Y" (valve is idle) for the current valve, we wait 1 sec
                time.sleep(1)  # We wait 1 sec
                Valve.Status(self)  # Check if the status has changed
                WaitingTime = WaitingTime + 1
                if WaitingTime >= 15.0:  # If the status has not changed in 15 sec there might be an error so we stop the "while" and write an error message
                    print("There is an error")
                    break

    def ValvePosition(self, MD):
        """
        The ValvePosition method is asking to a specific valve is current position.
        The user must indicate the name of the valve (Module adress).

        Parameters
        ----------
        MD : Module adress

        Returns
        -------
        """
        try:
            self.s.flushInput()  # Remove data from input buffer
            Position = str(MD) + "LQP\r"  # This str input ask to the valve is current position
            self.s.write(Position.encode())  # Send the command to the device encoded in UTF-8
            Line1 = self.s.read()  # First line give us useless information so we will not use it
            Output = self.s.read()  # Return the position of the valve (For example : "3" if the valve is in position 3)
            self.ValveState[
                "CurrentPosition" + str(MD)] = Output.decode()  # Save the position of the valve in the dictionnary
        except AttributeError:
            print("You have to open the connection if you want to communicate with the device")

    def ValveRotation(self, MD, pp):
        """
        The ValveRotation method is sending instructions to a specific valve in order to
        rotate the valve. The user must indicate the position of the valve as input and
        the name of the valve (Module adress). In order to optimize the rotation the method
        will choose rotate clockwis or counterclockwise depending of wich one is fastest.
        Parameters
        ----------
        MD : Module adress
        pp : Position

        Returns
        -------
        """
        try:
            if 0 >= pp or pp >= ValveConfigPosition[
                MD] + 1:  # Check if the valve number is fine or not depending of the valve configuration (Look Config.py)
                self.ValveState["Outrange"] = "Valve number is out of the limits"
                print("Wrong Value")
            else:  # The idea here is to calulate the oppoite number of our current position depending of the valve configuration
                if 1 <= self.ValveState["ValvePosition" + str(MD)] <= ValveConfigPosition[
                    MD] / 2:  # For example if we have 8 positions, the valve looks like this :   8  1  2
                    opposite = self.ValveState["ValvePosition" + str(MD)] + ValveConfigPosition[
                        MD] / 2  # 7     3
                else:  # 6  5  4
                    opposite = self.ValveState["ValvePosition" + str(MD)] - ValveConfigPosition[
                        MD] / 2  # So the opposite of 1 is 5; the opposite of 8 is 4; the opposite of 2 is 6; ........
                    # So we add 4 if our current position is lower or even at 4 and we substract 4 if our current position is 4 or upper

                if self.ValveState["ValvePosition" + str(
                        MD)] <= pp <= opposite:  # We check if: Current position < Target position < Opposite of current position (For example : 2<3<6)
                    string2Send = str(MD) + "LP0" + str(
                        pp) + "R\r"  # This str input move the valve in clockwise to target position
                    self.s.write(string2Send.encode())  # Send the command to the device encoded in UTF-8
                    self.ValveState["ValvePosition" + str(
                        MD)] = pp  # Change the Current position to the position where the valve will be at the end of the rotation
                    Valve.WaitForIdle(self)  # Wait until the movement is finished

                elif opposite <= pp <= self.ValveState["ValvePosition" + str(
                        MD)]:  # We check if: Opposite of current position < Target position < Current position (For example : 3<4<7)
                    string2Send = str(MD) + "LP1" + str(
                        pp) + "R\r"  # This str input move the valve in counterclockwise to target position
                    self.s.write(string2Send.encode())  # Send the command to the device encoded in UTF-8
                    self.ValveState["ValvePosition" + str(
                        MD)] = pp  # Change the Current position to the position where the valve will be at the end of the rotation
                    Valve.WaitForIdle(self)  # Wait until the movement is finished

                elif self.ValveState["ValvePosition" + str(
                        MD)] <= opposite <= pp:  # We check if: current position < Opposite of current position < Target position (For example : 1<5<7)
                    string2Send = str(MD) + "LP1" + str(
                        pp) + "R\r"  # This str input move the valve in counterclockwise to target position
                    self.s.write(string2Send.encode())  # Send the command to the device encoded in UTF-8
                    self.ValveState["ValvePosition" + str(
                        MD)] = pp  # Change the Current position to the position where the valve will be at the end of the rotation
                    Valve.WaitForIdle(self)  # Wait until the movement is finished

                elif opposite <= self.ValveState["ValvePosition" + str(
                        MD)] <= pp:  # We check if: Opposite of current position < current position < Target position (For example : 2<6<8)
                    string2Send = str(MD) + "LP0" + str(
                        pp) + "R\r"  # This str input move the valve in clockwise to target position
                    self.s.write(string2Send.encode())  # Send the command to the device encoded in UTF-8
                    self.ValveState["ValvePosition" + str(
                        MD)] = pp  # Change the Current position to the position where the valve will be at the end of the rotation
                    Valve.WaitForIdle(self)  # Wait until the movement is finished

                elif pp <= self.ValveState["ValvePosition" + str(
                        MD)] <= opposite:  # We check if: Target position < current position < Opposite of current position (For example : 2<3<7)
                    string2Send = str(MD) + "LP1" + str(
                        pp) + "R\r"  # This str input move the valve in counterclockwise to target position
                    self.s.write(string2Send.encode())  # Send the command to the device encoded in UTF-8
                    self.ValveState["ValvePosition" + str(
                        MD)] = pp  # Change the Current position to the position where the valve will be at the end of the rotation
                    Valve.WaitForIdle(self)  # Wait until the movement is finished

                elif pp <= opposite <= self.ValveState["ValvePosition" + str(
                        MD)]:  # We check if: Target position < Oppopsite of current position < current position (For example : 1<3<7)
                    string2Send = str(MD) + "LP0" + str(
                        pp) + "R\r"  # This str input move the valve in clockwise to target position
                    self.s.write(string2Send.encode())  # Send the command to the device encoded in UTF-8
                    self.ValveState["ValvePosition" + str(
                        MD)] = pp  # Change the Current position to the position where the valve will be at the end of the rotation
                    Valve.WaitForIdle(self)  # Wait until the movement is finished
        except AttributeError:
            print("You have to open the connection if you want to communicate with the device")
valve = Valve()
valve.OpenConnection()
valve.Status()

# Config for new-era pumps
port = Port('COM7', baud_rate=19200)
pri_pump = Pump(port, address = 0)
syr_pump = Pump(port, address = 1)
dead_volume = 5 # total dead volume in mL

# execute sequence commands:
import timeit
start = timeit.default_timer()

syr_pump.run(False)
valve.ValveRotation("a", 3)
sample(pri_pump)
backflush(pri_pump)
valve.ValveRotation("a", 2)
wash(pri_pump)
backflush(pri_pump)
valve.ValveRotation("a", 3)
stop = timeit.default_timer()
print('Time: ', stop - start)




