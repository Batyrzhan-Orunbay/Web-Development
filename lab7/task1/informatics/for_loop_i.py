# For Loop - Problem I: Count numbers divisible by k from 1 to n
n, k = int(input()), int(input())
count = 0
for i in range(1, n + 1):
    if i % k == 0:
        count += 1
print(count)
