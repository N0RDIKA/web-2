
a = float(input("Ведите a"))
b = float(input("Ведите b"))
c = float(input("Ведите с"))

if a < b and b < c:
    a = a + a
    b = b + b
    c = c + c

else:
    a = -a
    b = -b
    c = -c

print( a, b, c)