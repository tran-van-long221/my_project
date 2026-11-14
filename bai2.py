r = int(input())
if r <= 0 :
    print("Số được nhập không phải bán kính đường tròn")
else:
    cv = r*2*3.14
    dt = r*r*3.14
    print(f"{cv:.2f} {dt:.2f}", end = " ")