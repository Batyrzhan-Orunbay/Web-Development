n = int(input())
student_marks = {}
for _ in range(n):
    line = input().split()
    name = line[0]
    marks = list(map(float, line[1:]))
    student_marks[name] = marks

query = input()
marks = student_marks[query]
print(f"{sum(marks) / len(marks):.2f}")
