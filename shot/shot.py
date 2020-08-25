import sys
import random

max_value = sys.maxsize + 1
print(len(str(max_value)))
min_value = -max_value - max_value
with open('2-in.txt', 'w') as f:
    for i in range(100):
        flag = (random.random() > 0.5)
        factor = random.random() * max_value
        length = int(len(str(factor)) / 100 * (i + 1))
        result = str(int(factor))[:length] if flag else "-"+str(int(factor))[:length]
        f.write(result)
        f.write("\n")
