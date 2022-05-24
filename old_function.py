def Take_Cell_Samples(cellport, tube):
 """
 Sets valve to cell flask
 and pump infue of 5 mL + ygDV
 MISSING: cellport1, ygDV
 """
 valve.ValveRotation("a", cellport)
 # arm input to sample (instead of)
 # arm input to go to specific tube
 pri_pump.pumping_direction = PumpingDirection.INFUSE
 pri_pump.pumping_volume = 5 + ygDV
 pri_pump.pumping_rate = 75
 pri_pump.run()


def priFlush():
 """
 switches hamilton valve to air
 switches arm to waste
 and pump infuse yDV at max rate
 MISSING: yDV, air
 """
 valve.ValveRotation("a", airport)
 # arm function to switch to waste
 pri_pump.pumping_direction = PumpingDirection.INFUSE
 pri_pump.pumping_volume = yDV
 pri_pump.pumping_rate = 75
 pri_pump.run()


def cellBackflush(cellport):
 """
 Swicthes valve to cell port
 and pump withdraw at max rate for gDV
 MISSING: cellport1, gdv
 """
 valve.ValveRotation("a", cellport)
 pri_pump.pumping_direction = PumpingDirection.WITHDRAW
 pri_pump.pumping_volume = gDV
 pri_pump.pumping_rate = 75
 pri_pump.run()


def ywash():
 """
 washes the yellow tube
 swicthes hamilton to wash port
 swicthes arm to waste
 and pump infuse 3x ydv at max rate
 MISSING: yDV, wash
 """
 valve.ValveRotation("a", washport)
 # arm function to switch to waste
 pri_pump.pumping_direction = PumpingDirection.INFUSE
 pri_pump.pumping_volume = yDV * 3
 pri_pump.pumping_rate = 75
 pri_pump.run()


def blocking():
 """
 flushes cell to tube tubing
 with blocking/wash buffer
 MISSING: ygDV, cellport1
 """
 valve.ValveRotation("a", blockingport)
 # arm function to switch to waste
 pri_pump.pumping_direction = PumpingDirection.INFUSE
 pri_pump.pumping_volume = ygDV * 2
 pri_pump.pumping_rate = 0.5
 pri_pump.run()


def prime():
 """
 primes glycine and wash tubing
 pump ing gDV fof each tube
 MISSING: gDV, gly, wash
 """
 valve.ValveRotation("a", glyport)
 pri_pump.pumping_volume = gDV
 pri_pump.pumping_rate = 75
 valve.ValveRotation("a", washport)
 pri_pump.pumping_volume = gDV
 pri_pump.pumping_rate = 75
 pri_pump.run()


def gly(tube):
 """
 Switch hamilton valve to glycine
 perislatic pump 5 mL to tube
 """
 valve.ValveRotation("a", glyport)
 # arm input to sample (instead of waste)
 # arm command to go to speicifc tube
 pri_pump.pumping_volume = 5
 pri_pump.pumping_rate = 75
 pri_pump.run()