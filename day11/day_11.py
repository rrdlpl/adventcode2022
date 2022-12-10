import time


file = open('day11/input.txt', 'r')
lines = file.readlines()

start_time = time.time()

end_time = time.time()
print('Time ellapsed', (end_time - start_time) * 1000)

file.close()

