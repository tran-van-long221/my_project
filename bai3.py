a, b = map(int,input().split())
if a<= 0 or b <= 0 or a < b :
    print("Số nhập vào không thỏa mãn hình chữ nhật")
else:
    cv =(a+b)*2 
    dt = a*b 
    print(cv, dt, end = " ")