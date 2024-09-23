import math
from math import cos,atan,sin,sqrt,exp,log
a = 0.5
b = 2
h = 0.2

def func(x):
    if x < 1:
        return cos(sqrt(x**3))
    elif 1 <= x < 1.5:
        return atan(exp(x))  # arctg(e^x)
    else:
        return sin(log(x))**5  # sin^5(ln(x))



x = a
print(" x\t y")
while x <= b:
    print(f"{x:.1f}\t {func(x):.6f}")
    x += h