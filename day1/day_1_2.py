
import heapq

elves = open('inputs/day_1.txt', 'r')
elvesLines = elves.readlines()
weights = []
heap = heapq.heapify(weights)
sum = 0

for elf in elvesLines:
  if elf.strip() == '':
    heapq.heappush(weights, -sum)
    sum = 0 
    continue
  sum += int(elf.strip())

top1 = abs(heapq.heappop(weights))
top2 = abs(heapq.heappop(weights))
top3 = abs(heapq.heappop(weights))

print(top1 + top2 + top3)