import random
num = random.randint(1,100)
print("~~~~~~~~~~~~~~~~Welcome To The Random Guess Number Game~~~~~~~~~~~~~~~~~~")
a = 0
guesses = 0
while (a != num):
    guesses += 1
    a = int(input("Guess the Number: "))
    if (a > num):
        print("Lower Number Please")
    else:
        print("Higher Number Please")
print(f"You have guessed the number {num} correctly in {guesses} attempt")
