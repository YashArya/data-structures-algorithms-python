# 3. Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function

max = int(input("Enter a number: "))
odd_numbers = []

for i in range(1, max):
    if i % 2 != 0:
        odd_numbers.append(i)

print(f'odd numbers between 1 and {max} are: {odd_numbers}')