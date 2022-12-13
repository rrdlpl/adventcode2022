
import time


file = open('day13/input.txt', 'r')
lines = file.readlines()


def compare_lists(a, b):
    if isinstance(a, list) and isinstance(b, list):
        i = 0
        while i < len(a) and i < len(b):
            result = compare_lists(a[i], b[i])
            if result == True:
                return True
            if result == False:
                return False
            i += 1

        if i == len(a) and i < len(b):
            return True
        if i == len(b) and i < len(a):
            return False
        else:
            return None
    elif isinstance(a, list) and not isinstance(b, list):
        return compare_lists(a, [b])
    elif not isinstance(a, list) and isinstance(b, list):
        return compare_lists([a], b)
    else:
        if a < b:
            return True
        if a > b:
            return False
        else:
            return None


def sum_correct_pairs():
    sum = 0
    for i in range(0, len(lines), 3):
        a = eval(lines[i].strip())
        b = eval(lines[i + 1].strip())
        if compare_lists(a, b) == -1:
            pair_index = (i // 3) + 1

            sum += pair_index
    return sum


def merge_sort(packets):
    if len(packets) <= 1:
        return packets
    mid = int(len(packets) / 2)
    left = packets[0:mid]
    right = packets[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(a, b):
    array = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        result = compare_lists(a[i], b[j])
        if result == True:
            array.append(a[i])
            i += 1
        elif result == False:
            array.append(b[j])
            j += 1
        else:
            array.append(a[i])
            array.append(b[j])
            i += 1
            j += 1

    if i < len(a):
        array.extend(a[i:])

    if j < len(b):
        array.extend(b[j:])

    return array


def get_decoder_key():
    packets = []
    packets.append([[2]])
    packets.append([[6]])

    for i in range(0, len(lines), 3):
        a = eval(lines[i].strip())
        b = eval(lines[i + 1].strip())
        packets.append(a)
        packets.append(b)

    target1 = [[2]]
    target2 = [[6]]
    index1 = -1
    index2 = -1

    sorted_packets = merge_sort(packets)
    for packet in sorted_packets:
        print(packet)

    for i, arr in enumerate(sorted_packets):
        if arr == target1:
            print('aaaa', arr, i)
            index1 = i + 1
        if arr == target2:
            print('bbb', arr, i)
            index2 = i + 1
        if index1 > -1 and index2 > -1:
            break

    return index1 * index2


start_time = time.time()

result = sum_correct_pairs()
print('Solution 1', result)
decoder_key = get_decoder_key()
print('Solution 2', decoder_key)

end_time = time.time()


print('Time ellapsed', (end_time - start_time) * 1000)

file.close()
