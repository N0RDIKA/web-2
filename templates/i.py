a = int(input("Ведите целое число a "))
b = int(input("Ведите целове число b "))
s = 0
for i in range(1,a+1):
    p = 1.0
    for j in range(1,b+1):
        p *= i
    s += p
    

print("Sum = ", s)