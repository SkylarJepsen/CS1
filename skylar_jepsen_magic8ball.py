import random                                                               #add in the module random to use later
answers = ["yes", "no", "maybe", "ask again later"]                         #write all the possible answer options in list form
while True:                                                                 #start forever loop
    question = input ("What's your question?:")                             #ask question and allow response
    if "?" in question:                                                     #if there's a ? in the question then
        answer = (random.choice(answers))                                   #make the word answer the same as pick a random choice
        print (answer)                                                      #print a random option from the list
        break                                                               #break loop
    else:                                                                   #if answer is anything else without a ?
        print("that's not a question.")                                     #print text
if answer == "ask again later":                                             #if the answer was "ask again later" then
    while True:                                                             #start forever loop
        question_2 = input ("It's been a bit, what's your question?:")      #print text and allow for response
        if "?" in question_2:                                               #if theres a ? in their response
            print (random.choice(answers))                                  #then print a random option from list
            break                                                           #break loop
        else:                                                               #if answer is anything else without a ?
            print("that's not a question.")                                 #then print text



