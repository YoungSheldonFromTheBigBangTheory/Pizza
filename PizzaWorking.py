s = input("Large or Extra Large? ").lower()
while s != "large" and s != "extra large" and s != "l" and s != "xl":
    print("\nInvalid. Please enter a size.\n")
    s = input("Large or Extra Large? ").lower()
    
while True:
    try:
        t = str(input("How many toppings "))
        if float(t) in range(0, 5) and t.isnumeric() is True:
            t = float(t)
            break
        else:
            print("\nInvalid. Please enter amount, 0-4.\n")
    except ValueError:
        print("\nInvalid. Not an amount.\n")

if s.casefold() == "large" or "l": 
    st = 6
if s.casefold() == "extra large" or "xl":
    st = 10
    print(st)
if t != 0:
    st = (round(st+(0.0167*(t**3) - 0.1*(t**2) + 0.9333*(t) + 0.15), 2))
tax = round(st*0.13, 2)

print('\n' * 3 + s + " Size ")
print(int(t), "Toppings")
print("\nSubtotal    $" + str(st))
print("Tax         $" + str(tax))
print("Total       $" + str(round(float(st + tax), 2)))