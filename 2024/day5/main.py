from functools import cmp_to_key


file_a = open('2024/day5/input_aa.txt', 'r')
file_b = open('2024/day5/input_bb.txt', 'r')
order_lines = file_a.readlines()
page_number_lines = file_b.readlines()

page_ordering_rules = []
for line in order_lines:
    array = line.strip().split('|')
    page_ordering_rules.append((int(array[0]), int(array[1])))
    
page_numbers = []
for line in page_number_lines:
    line = [int(l) for l in line.strip().split(',')]
    line =tuple(line)
    
    page_numbers.append(line)
     
print(page_numbers)

page_ordering_rules = set(page_ordering_rules)
def part_one():
    total = 0
    for page_number in page_numbers:
        valid = True
        for i in range(len(page_number)-1):
            for j in range(i+1, len(page_number)):
                if (page_number[j], page_number[i]) in page_ordering_rules:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            total += page_number[len(page_number) // 2]
    return total


def part_two():
    def compare_func(a, b):
        if (a, b) in page_ordering_rules:
            return 1
        elif (b, a) in page_ordering_rules:
            return -1
        else:
            return 0
    key = cmp_to_key(compare_func)
    
    total = 0
    for page_number in page_numbers:
        valid = True
        for i in range(len(page_number)-1):
            for j in range(i+1, len(page_number)):
                if (page_number[j], page_number[i]) in page_ordering_rules:
                    valid = False
                    break
            if not valid:
                break
        if not valid:
            new_order = list(page_number)
            new_order.sort(key=key)
            total += new_order[len(new_order) // 2]
    return total


 
 
print('Solution 1', part_one())
print('Solution 2', part_two())