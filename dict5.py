The program takes a dictionary and prints the sum of all the items in the dictionary.
Problem Solution:
1. Declare and initialize the n number of dictionary values from the user.
2. Find the sum of all the values in the dictionary.
3. Print the total sum.
4. Exit.
Sample Input:
3
100
540
239
Sample Output :
879
# Step 1: Take the number of dictionary values from the user
n = int(input("Enter the number of items in the dictionary: "))

# Step 2: Initialize an empty dictionary
my_dict = {}

# Collect n values from the user
for i in range(n):
    key = input(f"Enter key for item {i + 1}: ")
    value = int(input(f"Enter value for item {i + 1}: "))
    my_dict[key] = value

# Step 3: Find the sum of all the values in the dictionary
total_sum = sum(my_dict.values())

# Step 4: Print the total sum
print(total_sum)
