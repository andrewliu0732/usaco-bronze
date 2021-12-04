
import sys
sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

numOfSwap = int(input())
num = [0, 1, 2]
count = [0, 0, 0]
for i in range(numOfSwap): # i = _
    a, b, g = map(int, input(). split())

    tmp = num[a-1]
    num[a-1] = num[b-1]
    num[b-1] = tmp

    count[num[g-1]] += 1

print(max(count))