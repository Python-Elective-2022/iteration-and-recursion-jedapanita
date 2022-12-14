"""
base:int or float
exp: int >= 0
returns: int or float, base^exp
"""
def iterativePower(base, exp):
    exp = int(exp)
    if exp >= 0:
        result = 1
        for time in range(int(exp)):
            result *= base

    return round(result, 2)
# test case
for i in range(0,5):
    n = iterativePower(3.3, i)
    print("n", n)

def recursivePower(base, exp):
    exp = int(exp)
    if exp >= 0:
        if exp == 0:
            result = 1
        else:
            result = base * recursivePower(base, int(exp) - 1)
    return round(result, 2)

for i in range(0,5):
    n = recursivePower(3.3, i)
    print("n", n)