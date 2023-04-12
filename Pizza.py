while True:

    

    s = input("Large or Extra Large? ").lower()
    while s != "large" and s != "extra large" and s != "l" and s != "xl":
        print("\nInvalid. Try Again\n")
        s = input("Large or Extra Large? ").lower()
    
    
    t = (input("How many toppings "))
    t = float(t)
    while t not in range(0, 5):
        print("\nInvalid. Try Again\n")
        t = (input("How many toppings "))
        t = float(t)

    if s.casefold() == "large" or "l": 
        st = 6
    elif s.casefold() == "extra large" or "xl":
        st = 10
    if t != 0:
        st = (round(st+(0.0167*(t**3) - 0.1*(t**2) + 0.9333*(t) + 0.15), 2))
    tax = round(st*0.13, 2)

    print("\nSize ")
    print("\nSubtotal    $" + str(st))
    print("Tax         $" + str(tax))
    print("Total       $" + str(round(float(st + tax), 2)))
    break