import math

def e(x, y):
    ansX = 0
    ansY = 0
    if x>0:
        ansX = -x * math.log(x,2)
    if y>0:
        ansY = -y * math.log(y,2)
    return ansX + ansY

print(e(2/5, 3/5) - 4/5 * e(1/2, 1/2) - 1/5 * e(0/1, 1/1))
print(e(3/5, 2/5) - 3/5 * e(2/3, 1/3) - 2/5 * e(0/2, 2/2))
print(e(2/5, 3/5) - 2/5 * e(1/2, 1/2) - 3/5 * e(1/3, 2/3))

