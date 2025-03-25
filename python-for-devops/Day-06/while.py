# while loop, used when we don't know how many times to repeat the loop

# Start with a number
number = 1

# Use a while loop to print numbers as long as the number is less than or equal to 5
while number <= 5:
    print(number)
    number += 1



# another while loop example

secret_number = 7

# Ask the user to guess a number
guess = int(input("Guess the secret number: "))

# Keep asking until the guess is correct
while guess != secret_number:
    print("Wrong guess. Try again!")
    guess = int(input("Guess the secret number: "))

print("Congratulations! You guessed the correct number!")

##############################################################################
##############################################################################

# break and continue

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print(number)

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    print(number)