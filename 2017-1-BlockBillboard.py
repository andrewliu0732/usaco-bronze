import sys
sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
tx1, ty1, tx2, ty2 = map(int, input().split())

# step 1. calculate total
area_a = (ay2 - ay1) * (ax2 - ax1)  # (5-2) * (3-1)
area_b = (by2 - by1) * (bx2 - bx1)
total = area_a + area_b

# step 2. calculate overlap (a)
tax1 = max(ax1, tx1)  # 1 2 = 2
tay1 = max(ay1, ty1)  # 2 1 = 2
tax2 = min(ax2, tx2)  # 3 8 = 3
tay2 = min(ty2, ay2)  # 5 3 = 3
area_xta = 0
area_yta = 0
if (tx1 < ax2): area_xta = tax2 - tax1
if (ty1 < ay2): area_yta = tay2 - tay1
area_ta = area_yta * area_xta
area_ta = max(area_ta, 0)

# step 3. calculate overlap (b)
tbx1 = max(bx1, tx1)
tby1 = max(by1, ty1)
tbx2 = min(bx2, tx2)
tby2 = min(ty2, by2)
area_xtb = 0
area_ytb = 0
if (tx1 < ax2): area_xtb = tbx2 - tbx1
if (ty1 < ay2): area_ytb = tby2 - tby1
area_tb = area_xtb * area_ytb
area_tb = max(area_tb, 0)

# step 4. find result
result = total - (area_ta + area_tb)
print(result)