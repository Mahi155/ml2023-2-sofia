# Ask the user for input N (positive integer)
N = int(input("Enter the value of N (positive integer): "))

# Initialize a list to store the N numbers
numbers = []

# Read N numbers one by one
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Ask the user for input X (integer)
X = int(input("Enter the value of X (integer): "))

# Check if X is in the list and find its index
if X in numbers:
    index = numbers.index(X) + 1
    print(f"The index of {X} is: {index}")
else:
    print("-1")
