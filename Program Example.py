from Operations import *
#start timer
initial_time = int(time.time()) #frame of reference in seconds
#delta_sleep(initial_time, minutes(1))

import timeit

start = timeit.default_timer()
end = timeit.default_timer()


start = timeit.default_timer()
startup()
end = timeit.default_timer()
print("startup()", end - start)

start1 = timeit.default_timer()
sample(1, 5)
end1 = timeit.default_timer()
print("sample()", end1 - start1)

start2 = timeit.default_timer()
quench(1)
end2 = timeit.default_timer()
print("quench()", end2 - start2)




