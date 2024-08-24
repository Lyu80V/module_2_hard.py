import random
n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
win = random.choice(n)
result = []
for i in range(1, win):
    for j in range(1,win):
        if win % (i + j) == 0 and i<j:
            result.append(i)
            result.append(j)

print(win, end=' : ')
print(*result, sep='')