import math


st = float(0)

while True:

    s = input("Large or Extra Large? ")
    t = float(input("How many toppings "))

    try:
        s = str(s)
    except ValueError:
        print("Invalid Size. Try Again")
        continue

    if s.casefold() == "large": 
        st = 6
    elif s.casefold() == "extra large":
        st = 10
    st = (round(st+(0.0167*(t**3) - 0.1*(t**2) + 0.9333*(t) + 0.15), 2))
    tax = st*0.13


    print("\nSubtotal    $" + str(st))
    print("Tax         $" + str(tax))
    print("Total       $" + str(round(float(st + tax), 2)))
    break