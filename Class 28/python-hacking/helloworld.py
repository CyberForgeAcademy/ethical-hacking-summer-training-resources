# Define a function to greet a user
def greet_user(name):
    print(f"Hello, {name}!")

# Initialize a list of names
names = ["Alice", "Bob", "Charlie"]

# Loop through each name in the list
for name in names:
    # Call the greet_user function with the current name
    greet_user(name)

# Calculate the sum of numbers from 1 to 10 using a loop
sum_numbers = 0
for i in range(1, 11):
    sum_numbers += i

# Print the result
print(f"The sum of numbers from 1 to 10 is: {sum_numbers}")
