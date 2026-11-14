a, h = map(int,input().split())
if a <= 0 or h <= 0 :
    print ("số được điền không thỏa mãn hình tam giác")
else:
    s = a*h/2
    print(f"{s:.2f}")