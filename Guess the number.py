import random

def main():
    # secret number between 1,99
    secret_number=int(random.randint(1,99))
    guess=int(input("Guess the number "))

    while guess!=secret_number:
        if guess<secret_number:
            print("The guess is too low!")
        elif guess>secret_number:
            print("guess is too high")
        guess=int(input("Guess the number again"))


    print("Congratulations your guess is right and the number is ",secret_number)

if __name__ == '__main__':
        main()