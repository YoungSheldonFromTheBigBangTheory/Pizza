import math

st = float(0)
z = 0

while True:

    

    s = input("Large or Extra Large? ").lower()
    while s != "large" and s != "extra large" and s != "l" and s != "xl":
        print("\nInvalid. Try Again\n")
        s = input("Large or Extra Large? ").lower()
    
    
    #t = str(input("How many toppings "))
    #print (float(t))
    #t = float(t)
    #while float(t) not in range(0, 5) and t.isnumeric() is True:
        #print("\nInvalid. Try Again\n")
        #t = (input("How many toppings "))
   
    while z == 0:
        try:
            t = str(input("How many toppings "))
            if float(t) in range(0, 5) and t.isnumeric() is True:
                z = 1
            else:
                print("\nInvalid. Try Again\n")
                t = t + t
        except ValueError:
            print("\nInvalid. Try Again\n")
            #t = (input("How many toppings "))
        #else:
            #z = 1
            #t = float(t)


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