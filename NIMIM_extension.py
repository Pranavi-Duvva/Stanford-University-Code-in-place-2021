


def main():
    """"
    AI for Game of Nimm

    Task:
    Pick some positive integer and call it n.
    If n is even, divide it by two.
    If n is odd, multiply it by three and add one.
    Continue this process until n is equal to one.
    """

    # user input for the number
    # validate number if it's negative
    # check if number is even or odd
    number=get_number()
    counter=0
    while number!=1:
        number=check_even_odd(number)
        counter +=1
    print("The process took",counter,"steps to reach 1")




def check_even_odd(number):
    """
    This function checks if the number is even or odd
    if number is even it is divided by 2
    if number is odd multiply by 3 and add +1
    """
    if number%2==0:
        new_number=int(number/2)
        print(str(number)+" is even, so I take half:",new_number)
        number=new_number
        return number
    if number%2!=0:
        new_number=int((3*number)+1)
        print(str(number) + " is odd, so I make 3n+1:",new_number )
        number=new_number
        return number





def get_number():
    while True:
        number=int(input("Enter a number: "))
        if is_valid(number):
            return number
        print("Enter valid positive number greater than 0")
    return number

def is_valid(number):
    if number>=1:
        return True
    else:
        False












if __name__ == '__main__':
    main()