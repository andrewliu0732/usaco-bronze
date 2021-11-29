import sys
sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")


a, b = map(int, input().split())
c, d = map(int, input().split())

# step 1. calculate total
farmer_painted = b - a
bessie_painted = d - c
total = farmer_painted + bessie_painted

#step 2. find overlap
overlap_case1 = min(b, d) - max(a, c)  # -2
overlap = 0
if overlap_case1 >= 0:
    overlap = overlap_case1

# step 3. result
result = total - overlap
print(result)
