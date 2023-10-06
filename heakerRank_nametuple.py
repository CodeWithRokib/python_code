
from collections import namedtuple

n = int(input())
Student = namedtuple('Student', input())

total = 0
for _ in range(n):
    s = Student(*input().split())
    total += int(s.MARKS)

print(f'{total / n:.2f}')