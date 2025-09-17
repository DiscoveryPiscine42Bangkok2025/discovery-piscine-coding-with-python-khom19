num = int(input("Enter a number less than 25\n"))
if num > 25: 
    print("Error")
else: 
    while True:
        print(f"Inside the loop, my variable is {num}")
        if num == 25:
            break
        num += 1