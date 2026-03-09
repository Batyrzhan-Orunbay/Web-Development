n = int(input())
scores = list(map(int, input().split()))
scores = sorted(set(scores), reverse=True)
print(scores[1])
