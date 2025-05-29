import time     
import os       
import random
import csv

def add_entry(websites, usernames, passwords):
    '''
    Adds an entry to the parallel array of websites, usernames, and passwords
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    Returns:
        parallel array: newly added to array of websites, usernames, and passwords
    '''
    while True:
        website = input("Enter website. Press 'q' to end: ")

        if website == 'q':
            break 
        username = input('Enter username: ')
        password = input('Enter password (Press "g" to generate): ')

        if password.lower() == "g":
            while True:
                password = generate_password()
                generate = input(f'The generated password is {password}. Enter "c" to continue or "g" to generate again ').lower()

                if generate == "c":
                    break
                elif generate == "g":
                    continue
                else:
                    print("invalid")
        websites.append(website)       
        usernames.append(username)
        passwords.append(password)
def print_entry(website, username, password):
    '''
    Prints a set of a website with the corresponding username and password
    Args:
        website (str): The user's entered website
        username (str): The user's entered username
        password (str): The user's entered password
    Returns: 
        f-string: prints the user's corresponding website, username, and password
    '''
    print(f'''
Website: {website}
Username: {username}
Password: {password} ''')
def print_entries(websites, usernames, passwords):
    '''
    Takes three elements (a website, username, and password trio) and prints them neatly in an f-string
    Args:
        websites (list of str): a list containing website names
        usernames (list of str): a list containing corresponding usernames for each website
        passwords (list of str): a list containing corresponding passwords for each website
    Returns:
        none
    '''
    for i in range(len(websites)):                                              #goes through each website in the list
        print_entry(websites[i], usernames[i], passwords[i])                    #print the corresponding website, username, and password neatly in an f-string
def get_index(websites):
    '''
    Takes a list of websites and returns index of websites in the list
    Args:
        websites (list): the list of websites
    Returns:
        index: website in given list of websites
    '''
    while True:
        web = input('Please enter a website: ')

        if web in websites:
            return websites.index(web)                                          #if the website is in the list, store the index of where in the list it is
        else:
            print('Website is not here.')
def change_entry(websites, entry_list, entry_type, usernames, passwords):
    '''
    Takes an entry and allows user to change it
    Args:
        websites (list of str): the full list of user's websites
        usernames (list of str): the full list of user's usernames
        passwords (list of str): the full list of user's passwords
        entry_list (list of str): the list to update entries
        entry_type (str): a string indicating which type of entry is being changed
    Returns:
        print: new entry
    '''
    index = get_index(websites)                                                 #find the index of the website that the user wants to change in the list of websites
    entry_list[index] = input(f'Please enter the new {entry_type}: ')           #Ask the user for the new value and update the entry in the list
    print(f'{entry_type} updated to: {entry_list[index]}')
    print_entry(websites[index], usernames[index], passwords[index])
def delete_entry(websites, usernames, passwords):
    '''
    Takes an entry and allows user to delete it
    Args:
        websites (list of str): the full list of user's websites
        usernames (list of str): the full list of user's usernames
        passwords (list of str): the full list of user's passwords
    Returns:
        none
    '''
    index = get_index(websites)
    websites.pop(index)                                                             #find the index of the entry to delete
    usernames.pop(index)
    passwords.pop(index)
def get_password_length(characters):
    '''
    Gets a password length from the user to be used later
    Args:
        characters (list of str): a list of characters that can be used to generate the password
    Returns:
        int: the user-defined password length
    Raises:
        try ValueError: if the user's input is not a valid integer
    '''
    while True:
        try:                                                                        #try to convert the user's input to an integer
            length = int(input('Please enter your desired password length: '))      #ask the user to enter a desired password length

            if length > 3 and length < len(characters):
                return length
            else:
                print(f'Please enter a number between 4 and {len(characters)}')
        except ValueError:                                                          #if the user does not enter an integer, instead of causing a ValueError then
            print('Please enter an integer.')
def check_security(pwd, length, display):
    '''
    Checks the security of a given password
    Args:
        pwd (str): The password to evaluate
        length (int): The minimum required length of the password
        display (bool): If True, prints whether the password is secure or not
    Returns:
        bool: True if the password meets the criteria, False if not
    '''
    if len(pwd) < length or pwd == pwd.lower() or pwd == pwd.upper() or not any(char.isdigit() for char in pwd) or not any(char in pwd for char in list('`~@#$%^&*()-_=+')):
        if display:
            print(f'{pwd} is not secure')
        return False
    else:
        if display:
            print(f'{pwd} is secure')
        return True
def generate_password():
    '''
    Generates a random password with a set length
    Args:
        None
    Returns:
        str: randomly generated password
    '''
    characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&_*()-+=')                 #list of all allowed characters for the password
    length = get_password_length(characters)                                        #ask the user how long the password should be

    while True:
        pwd = ''.join(random.sample(characters, length))                            #randomly pick characters and join them into a password string

        if check_security(pwd, length, False):
            return pwd                               
def clear_console(delay):
    '''
    Pauses for a short time, then clears the screen

    Args:
        delay (float): The number of seconds to wait before clearing the screen
    Returns:
        None
    '''
    time.sleep(delay)                                                               #wait for the specified number of seconds before clearing
    os.system('cls')                                                                #clear the console
def export_to_csv(filename, headers, *arrays):
    '''
    Exports parallel arrays to a CSV file.

    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    Returns:
        None
    Raises:
        ValueError: If no arrays are provided, or is arrays are not the same length
    '''
    if not arrays:                                                      #if no array is given
        raise ValueError("At least one array must be provided.")        #acknowledges an error and controls it
    
    num_rows = len(arrays[0])                                           #creates the number of rows using the number of elements in the first array

    for arr in arrays:                                                  #checking that for every array
        if len(arr) != num_rows:                                        #the lengths are all the same
            raise ValueError("All arrays must have the same length.")   #controls error if lengths are different
    
    with open(filename, 'w', newline='') as csvfile:                    #open the file in writing mode
        csvwriter = csv.writer(csvfile)                                 #creates writer to write data in the file
        csvwriter.writerow(headers)                                     #writes the first row as headers

        for i in range(num_rows):                                       #for the number of rows
            row = [arr[i] for arr in arrays]                            #creates each row of data using the element in the arrays
            csvwriter.writerow(row)                                     #writes each row of data to the csv file
def main():
    websites = []
    usernames = []
    passwords = []

    secret_code = input('Enter your secret code or press "g" to generate password: ')
    
    if secret_code.lower() == 'g':
        secret_code = generate_password()
        print(f'Your secret code is {secret_code}')
        clear_console(6)
    else:
        print('Secret code valid')
        clear_console(2)

    add_entry(websites, usernames, passwords)
    tries = 3

    for i in range(tries):
        entry = input('Please enter password to enter the Password Keeper or enter "q" to quit: ')
        
        if entry == 'q':
            exit()
        elif entry == secret_code:
            print('Access granted!')
            clear_console(1)
            break
        else:
            print('Access denied, try again!')
            clear_console(1)
        
    if entry != secret_code:
        print('Access denied.')
        clear_console(1)
        exit()
    
    options = '''
1. Add an entry: Adds an entry to the parallel array of websites, usernames, and passwords
2. Access specific entry: Allows user to enter a website and prints the website, username, and password of said website
3. See all entries: Displays all entries
4. Change an entry: Takes an entry and allows user to change it
5. Delete an entry: Takes an entry and allows user to remove it
6. Check a password for security: Takes a password and checks its security
7. Generate a password: Generates a random password
8. Export entries: Exports entries to CSV
    '''
    print(options)

    while True:
        option = input('What would you like to do? Enter "o" to see the options or enter "q" to quit. ').lower()

        if option == "q":
            break
        elif option == "o":
            print(options)
        elif option == "1":
            add_entry(websites, usernames, passwords)
        elif option == "2":
            index = get_index(websites)
            print_entry(websites[index], usernames[index], passwords[index])
        elif option == "3":
            print_entries(websites, usernames, passwords)
        elif option == "4":
            change = input('Would you like to change a 1. website, 2. username, or 3. password? Enter "q" to end: ')

            if change == 'q':
                break
            elif change == '1':
                change_entry(websites, websites, "website", usernames, passwords)
            elif change == '2':
                change_entry(websites, usernames, "username", usernames, passwords)
            elif change == '3':
                change_entry(websites, passwords, "password", usernames, passwords)
            else:
                print('Invalid Response.')
        elif option == '5':
            delete_entry(websites, usernames, passwords)
        elif option == '6':
            check = input('Enter a password or press "p" to check a specific password: ')
            length = get_password_length()

            if check.lower() == "p":
                index = get_index(websites)
                check_security(passwords[index], length, True)
            else:
                check_security(check, length, True)
        elif option == '7':
            password = generate_password()
            change_pwd = input(f'The generated password was {password}. Would you like to replace a specific password? y/n ')

            if change_pwd.lower() == 'y':
                index = get_index(websites)
                passwords[index] = password
        elif option == '8':
            filename = input('Enter a filename for your csv: ')
            export_to_csv(filename+".csv", ["Website", "Username", "Password"], websites, usernames, passwords)
        else:
            print('Invalid Response.')
main()