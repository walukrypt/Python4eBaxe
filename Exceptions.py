while True:
   try:
    x = int(input("venza  car brake fails car dealer dies suddenly for the number you input, so whats your number?"))
    break
   except ValueError:
    print("x is not an integer")
   else:       
    print(f"x is {x}")    
