dictionary = {i: chr(i) for i in range(97, 123)}
last = 256
arr = [97, 97, 98, 256, 258, 257, 259]

result = []
p = arr.pop(0)
result.append(dictionary[p])

for c in arr:
    if c in dictionary:
        entry = dictionary[c]
    result.append(entry)
    dictionary[last] = dictionary[p] + entry[0]
    last += 1
    p = c

print(''.join(result))