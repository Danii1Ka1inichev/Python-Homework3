from collections import Counter

line = [1, 1, 2, 2, 7, 12, 10]
counter = dict(Counter(line))
max_repeat = 0
max_list = []
for i in counter:
    if counter[i] == 1:
        continue
    else:
        if counter[i] > max_repeat:
            max_list = []
            max_repeat = counter[i]
            max_list.append(i)
        if counter[i] == max_repeat:
            max_repeat = counter[i]
            max_list.append(i)
max_list = set(max_list)
print(max_list)
