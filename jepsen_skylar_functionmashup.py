import random        #storing random to be used later

def chorus():
    '''
    Prints the chorus of a song
    Args:
        None
    Returns:
        print: chorus
    '''
    print ('''
    So I put my hands up
    They're playin' my song, the butterflies fly away
    I'm noddin' my head like, yeah
    Movin' my hips like, yeah
    I got my hands up, they're playin' my song
    They know I'm gonna be okay
    Yeah, it's a party in the U.S.A.
    Yeah, it's a party in the U.S.A.
    ''')

def sing_song():
    '''
    Prints the lyrics of a song
    Args:
        None
    Returns:
        print: song and chorus
    '''
    chorus()
    print ('''
    I hopped off the plane at LAX
    With a dream and my cardigan
    Welcome to the land of fame excess (whoa)
    Am I gonna fit in?
    ''')
    chorus()

def add(x, y):           
    '''
    Takes two numbers and adds them together
    Args:
        x (int): first number
        y (int) second number
    Returns:
        None (prints sum of x and y)
    '''                                            
    print(x+y)      #print the sum of the two numbers 

def print_list(array):
    '''
    Takes a list and prints every element in that list individually (vertically)
    Args:
        list (classes)
    Returns:
        print: every element in list vertically
    '''
    for i in array:     #for the element in the list
        print (i)       #print each element

def in_list(element, array):      
    '''
    Takes a list and element and returns a boolean based on if the element is in the list
    Args:
        array: list (classes)
        element
    Returns:
        int: the entered integer
    '''
    return(element in array)        #store the product(the element in the list)

def get_integer(order):
    '''
    Takes any parameter and returns a boolean based on if the element is in the list
    Args:
        any parameter
    Returns:
        print: boolean based on if the element is in the list
    Raises:
        try ValueError
    '''
    while True:         #create a forever loop
        try:            #test
            number = int(input(f'Please enter your {order} number: '))      #ask the user for two numbers
            return number                                                   #store that number
        except ValueError:                                                  #unless there is a value error
            print('Not an integer!')                                        #tell user to enter an integer

def get_integers():
    '''
    Asks the user for two numbers, uses is_integer to check input, returns the two integers
    Args:
        num1
        num2
    Returns:
        tuple: num1, num2
    Raises:
        is_integer
    '''
    a = get_integer('first')        #make a symbolize the first number
    b = get_integer('second')       #make b symbolize the second number
    return a, b                     #store the two numbers
        
def get_random():
    '''
    Uses get_integers and prints a random number between the two given integers
    Args:
        get_integers: a, b
    Returns:
        print: random numbr between two integers
    '''
    while True:                     #create forever loop
        a, b = get_integers()       #call the function to get two integers from that output

        if a > b:                   #check if the first integer is greater than the second
            print('Please make sure your first number is less than your second!')       #tell user to enter a second number that is less than the first
        else:                       #if the first number is what was expected
            print(random.randint(a, b))     #print a random integer between a and b
            break                   #exit the loop

def count_vowels(string):
    '''
    counts the number of vowels in the given string and tells the user
    Args:
        string: the input string in which vowels will be counted
    Returns:
        str: a message stating the total number of vowels in the string
    '''
    count = 0                               #set the starting vowel count to 0
    vowels = ['a', 'e', 'i', 'o', 'u']      #list of vowels to check for
    for char in string:                     #look at each letter in the string
        if char.lower() in vowels:          #if the letter is a vowel, count it
            count+=1                        #add 1 to the count if it's a vowel
    return f'There are {count} vowels.'     #print the result

def subtract(x,y):
    '''
    Subtracts two numbers and prints the difference
    Args:
        x: the first number
        y: the second number
    Returns:
        None
    '''
    print(x-y)      #print the difference

def multiply(x,y):
    '''
    Multiplies the two numbers and prints the product
    Args:
        x: the first number
        y: the second number
    Returns:
        None
    '''
    print(x*y)      #print the product

def divide(x,y):
    '''
    Divides the first number by the second and prints the quotient. If the second number is zero, it prints a message instead
    Args:
        x: the first number
        y: the second number
    Returns:
        None
    '''
    if y == 0:      #if second number is 0
        print("Cannot divide by zero!Enter a new integer.")     #tell the user it cannot be divided
    else:           #if not
        print(x/y)  #print the quotient

def main():         #calls all functions
    while True:     #forever loop

        option = input('What would you like to do? 1. Sing a song, 2. Enter calculator mode, 3. Experiment with lists, or 4. Count vowels?: ')  #asks the user what they want to do

        if option == '1':   #if user picks the first option
            sing_song()     #calls the sing_song function to sing a song

        elif option == '2': #if user picks the second option
        
            operation = input('What would you like to do? Get a random number(random), +, -, *, /: ')   #asks the user what kind of calculation they want to do
            if operation == 'random':   #if user picks 'random'
                get_random()            #call get_random function to print a random number within a range
            
            elif operation in ['+', '-', '*', '/']:     #if the user selects any arithmetic operation
                a, b = get_integers()   #calls get_integers function to get two numbers from the user
            
                if operation == '+':    #if user wants to add
                    add(a, b)           #calls the add function to calculate and print the sum
                elif operation == '-':  #if the user want to subtract
                    subtract(a, b)      #calls the subtract function to calculate and print the difference
                elif operation == '*':  #if the user wants to multiply
                    multiply(a, b)      #calls the multiple function to calculate and print the product
                elif operation == '/':  #if the user wants to divide
                    divide(a, b)        #calls the divide function to calculate and print the quotient
            else:                       #if user enters anything else
                    print('Invalid Response.')        #tell the user their input is invalid

        elif option == '3':             #if the user picks the third option
            which_function = input('Do you want to 1. Print and identify items in a list, or 2. Create your own list?: ') #asks the user which function they want to use

            if which_function == '1':   #if the user picks the first option
                classes = ['english', 'science', 'history', 'math', 'computer science'] #predeifned list of classes
                print_list(classes)     #calls print_list function to display the list
                user_input1 = input('Enter a class to check if it is in your scheduled classes: ')    #asks the user to enter a value to check if its in the list
                print(in_list(user_input1, classes))      #checks if the users input is in the classes list
            elif which_function == '2': #if the user picks the second option
                user_list = input('Enter your list of items, separate each item using a space ').split(' ')     #asks the user to input a list of items
                print_list(user_list)   #calls print_list function to display the users created list
            else:                       #if user enters anything else
                print('Invalid Response.')                 #exit code
                continue

        elif option == '4':             #if the user picks the fourth option
            user_input2 = input('Enter a phrase or word: ')      #asks the user to enter a phrase or word
            print(count_vowels(user_input2))                     #calls the count_vowels function to count and print the amount of vowels in a given phrase/word
        
        else:                           #if user enters anything else
            print('Invalid Response.')  #print invalid message
        
        play_again = input("Would you like to play again? yes/no: ").lower()        #asks the user if it wants to play again
        if play_again == 'no':          #if the user enters 'no'
            print("Thanks for playing!")    #print goodbye message
            break                           #exit loop and break out of program
        elif play_again != 'yes':       #if the user answers anything other than 'yes'
            print('Invalid Response. Thanks for playing!') #prints invalid and goodbye message
            break                       #exits loop and breaks out of program
main()                                  #calls the main function to run the program