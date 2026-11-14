import math
a, b, c =map(int,input().split())
if a > 0 and b > 0 and c > 0 and (a+b) > c and (b+c) > a and (c+a) > b :
    p = (a+b+c)/2 
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    R = (a*b*c)/(4*S)
    print(f"{R:.3f}")
else:
    print("Số nhập vào không thỏa mãn điều kiện của tam giác")