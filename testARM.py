from functions import Arm

arm = Arm()
arm.OpenConnection()

num = 1
arm.goTube(num)
arm.Valve('waste')
