string = "thisistheythought"
dictionary = {chr(i): i for i in range(97, 123)}

last = 256
p = ""
result = []

for c in string:
    pc = p + c
    if pc in dictionary:
        p = pc
    else:
        result.append(dictionary[p])
        dictionary[pc] = last
        last += 1
        p = c

if p != '':
    result.append(dictionary[p])

print(result)