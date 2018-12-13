a = int(input())
b = int(input())
if a == 0 and b == 0:
    print("INF")
elif (a == 0 and b != 0) or -b/a!=int(-b/a):
    print("NO")
elif a!=0:
    print(int(-b/a))
