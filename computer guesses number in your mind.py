
"""
    This program guesses the number in your mind

    If the guessed number is higher than the number in your mind
    Type higher

    If the guessed number is lower than the number in your mind
    Type lower

    If the guessed number is correct than the number in your mind
    Type correct


"""

MAX_NUMBER=100
MIN_NUMBER=1
import random

def main():

    # Computer guesses a random number between 1 and 100
    secret_number=random.randint(1,100)
    max_number=MAX_NUMBER
    min_number=MIN_NUMBER

    #Taking the user response if the guess is higher or lower than the actual number
    response=(input("Is your number "+str(secret_number)+"? "))

    #Saving  the last guessed number
    last_number=int(secret_number)

    # initializing a counter to calculate the number of guesses
    counter=1

    while response!="correct":

        if response=="higher":

                max_number=max_number
                # since the response is higher than last number adding 1
                min_number=last_number+1
                secret_number=random.randint(min_number,max_number)

        else:

            # since the response is lower than last number subtracting 1
            max_number=last_number-1
            min_number=min_number
            secret_number = random.randint(min_number, max_number)

        last_number=secret_number
        #print("max_number",max_number)
        #print("min_number",min_number)
        counter=counter+1

        response = (input("Is your number " + str(last_number) + "? "))

    print("I win! It took me " +str(counter)+" guesses")
















if __name__ == '__main__':
        main()