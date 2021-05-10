
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

    #Taking the user response if the guess is higher or lower than the actual number also validating user response

    response=get_response(secret_number)

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

        response=get_response(last_number)


    print("I win! It took me " +str(counter)+" guesses")



def get_response(secret_number):

    while True:

        # Takes the user input while True
        response = (input("Is your number " + str(secret_number) + "? "))
        # converts the response in to lower case
        response = response.lower()


        # validates response
        if is_valid(response):
            # if the its a valid response this will return the response
            return response

        # Else it will ask user to enter response again

        print("invalid response enter higer or lower")
    return response

def is_valid(answer):

    """
    validates user input if the typed word is either lower or higher or correct
    This function return true if its a valid input
    
    If it is not any of the above three words this function  will return false

    """

    if answer=="higher" or answer=="lower":
        return True
    if answer=="correct":
        return True

    else:
         False













if __name__ == '__main__':
        main()