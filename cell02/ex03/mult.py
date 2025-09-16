first = int(input("Enter the first number:\n"))
second = int(input("Enter the second number:\n"))
val = first*second

print(f"{first} x {second} = {val}")
if val > 0 : print("The result is positive.")
elif val < 0 : print("The result is negative.")
else : print("The result is positive and negative.")