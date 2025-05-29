#Author: Skylar Jepsen
#Description: This code allows multiple users to plan their meal for the day, randomly picking the main, sides, and dessert, while the user can choose the drinks.
#Date: Apr 4, 2025
#Bugs: none
#Challenges: Adding dessert and drinks with prices, addressing multiple users, calculating the total cost, ensuring that the user enters a valid integer, and adding an additional option to not dine
#Sources: none

import random   #add random function to be used later

mains = ['cauliower', 'tilapia fillet', 'pork loin', 'salmon', 'three color squash', 'eggplant', 'steak', 'baguette']   #create options of mains
prices = [20, 25, 28, 30, 18, 20, 22, 30, 20]    #create options of prices aligning with mains
flairs = ['with balsamico', 'with garlic and olive oil', 'with minted yogurt' 'with chutney', 'with salad', 'with salsa', 'over sticky rice', 'au jus', 'with basmati rice']    #create options of sides
desserts = ['brownie', 'cookie skillet', 'sorbet', 'lava cake', 'cake']    #create options of desserts
dessert_prices = [12, 17, 13, 17, 15]    #create options of prices aligning with desserts
drinks = ['still water', 'sparkling water', 'diet coke', 'coke', 'shirley temple', '']  #create options of drinks
drink_prices = 2    #set all drinks $2

while True: #create forever loop
    start = input('Welcome to the food-o-matic! Would you like to order? y/n: ')    #ask what they want to order

    if start == 'n':    #if they respond with 'n'
        break   #then break out of loop
    elif start != 'n' and start != 'y': #if they respond with neither 'n' or 'y'
        print('Invalid response')   #print invalid response
        continue    #restart

    try:    #if an error occurs
        items = int(input('How many menu items will you be ordering: '))    #ask how many items they will order
    except ValueError:  #if there is an error with the value
        print('Enter an integer')   #ask them to enter an integer
        continue    #restart

    total = 0   #set the total to 0

    for i in range(items):  #for a item in items
        main = random.choice (mains)    #pick a random choice from the list mains
        flair = random.choice (flairs)  #pick a random choice from the list flairs
        price = prices[mains.index(main)]   #pick the price corresponding to the main
        total += price  #add the price to the total
        print(f'Person {i+1}, your dish is {main} {flair}, ${price}')   #tell the user their main, flair, and price
    
    print(f'Your total is: ${total}')   #tell the user the new total price

    dessert = input(f'Do you want dessert? yes/no: ').lower()   #ask if user wants dessert

    if dessert == 'yes':    #if they say 'yes'
        for i in range(int(items)): #for a item in items
            dessert = random.choice(desserts)   #pick a random choice from the list desserts
            dessert_price = dessert_prices[desserts.index(dessert)] #pick the price corresponding to the dessert

            if dessert == 'sorbet' or dessert == 'cake':    #if the dessert is 'sorbet' or 'cake'
                flavor = input(f'Which flavor of {dessert} would you like? ')   #ask user what flavor they want
                dessert = flavor + ' ' + dessert    #use their response as the flavor

            print(f'Person {i+1}, your dessert is {dessert}')   #tell user #1 what their dessert is
            total += dessert_price  #add dessert price to the total

        print (f'Your total is: ${total}')  #tell them what their new total price is

    drink = input('Do you want drinks? yes/no: ').lower()   #ask the user if they want drinks

    if drink == 'yes':  #if they say 'yes'
        for i in range(int(items)): #for a item in items
            which_drink = input(f'Person {i+1}, Which drink do you want? still water/sparkling water/diet coke/coke/shirley temple: ' )     #ask user #1 what drink they want
            print(f'Your drink is {which_drink}, $2')   #tell the user their drink and the price
            total += 2  #add the price to the total
            
        print (f'Your total is: ${total}')  #print the new total price
        break   #break out of loop

    elif drinks == 'no':    #if they say 'no'
        break   #break out of loop