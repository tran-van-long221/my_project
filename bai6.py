import math
a, b, c = map(int,input().split())
if a > 0 and b > 0 and c > 0 and a+b > c and b+c > a and c+a > b :
    cv = a+b+c 
    p = cv/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"{cv:.1f} {s:.3f}")
else:
    print("3 số không thỏa mãn hình tam giác")