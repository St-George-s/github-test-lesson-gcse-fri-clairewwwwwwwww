# This is a loop that prints hello 10000 times
#claire is the variable
for claire in range(1000):
    print("Claire")         

#ask for a number from the user
number=int(input("Enter a number for the times table: "))
#calculate and print the times table for the entered number up to 12
for(i) in range(1,13):
    print(str(number)+"x"+str(i)+"="+str(number*i))

name = input("What is your name? ")
print("Hello, " + name)

# This is a single-line comment in Python
print("Hello, World!")  # This is a comment after code

# This for loop will print your name 10 times.
for i in range(10):
    print("Your Name")


    # Ask for a number from the user
number = int(input("Enter a number for the times table: "))

# Calculate and print the times table for the entered number up to 12
for i in range(1, 13):
    # Concatenation of strings and type casting of integer to string
    print(str(number) + " x " + str(i) + " = " + str(number * i))


    total_age = 0
for i in range(10):
    age = int(input(f"Enter the age of person {i+1}: "))
    total_age += age  # Adds the age to the running total
print("The total age is: " + str(total_age))