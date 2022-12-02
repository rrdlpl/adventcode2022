
import heapq

elves = open('input.txt', 'r')
elvesLines = elves.readlines()


maximum = -1 
sum = 0
weights = []
heap = heapq.heapify(weights)

for elf in elvesLines:
  if elf.strip() == '':
    maximum = max(sum, maximum)
    sum = 0 
    continue
  sum += int(elf.strip())
  
print(maximum)