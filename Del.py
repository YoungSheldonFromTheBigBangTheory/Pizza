import math

while True:

    d = input("Diameter ")

    try:
        d = float(d)
    except ValueError:
        print("Invaild")
        continue

    r = d/2

    p = math.pi

    a = float(p * (r **2))

    c = float(2 * p * r)

    b = str(a)

    d = str(c)

    print("Circumernce " + d)
    print("Area " + b)
    break