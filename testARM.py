# arm = Arm()
# arm.OpenConnection()
#
# num = 1
# arm.goTube(num)
# arm.Valve('waste')
y = '1, 2, 3, 4'
txt = [x.strip() for x in y.split(',')]

x = 2
def test(txt):
    for i in range(len(txt)):
        global x
        x = 4


test(txt)

print(x)
