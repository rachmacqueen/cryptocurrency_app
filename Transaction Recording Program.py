# Name: Rachel Sanders
# This application was created as an assignment for the Cryptographic Concepts unit, as part of Edith Cowan University's Y89 Bachelor of Science (Cyber Security)
# Python 3.6.5 was used for this assignment


# Import the required modules
import datetime as date                                                                 #allows for creating a timestamp of the current date/time
import os                                                                               #allows for operating system procedures such as reading of file statistics
       
#This function repeatedly prompts for input until a string (and no whitespace) is entered.
def user_string_input(prompt):
    while True:
        value = input(prompt).strip()      
        if value.isalpha():
            return value
            break;
        else:
            print('\nA valid input is required - Please enter at least one character (ALPHABETIC CHARACTERS ONLY). \n')
            continue

#This function repeatedly prompts for input until an integer (and no whitespace) is entered.
def user_int_input(prompt):
    while True:
        value = input(prompt).strip()      
        if value.isdigit():
            return value
            break;
        else:
            print('\n\nAn valid input is required - Please enter at least one character (NUMERIC CHARACTERS ONLY). \n')
            continue
             

#start of program
while True:
        first_trans = True
        print('\nWelcome to the Transaction Recording Program! This application allows you to add new transactions to a Transaction File, which will then be added as a new block to a block chain! \nPlease press any key to begin, or else press [q] to quit.')
        choice = input('> ')
        if choice.lower() == 'q':
                print('\nFarewell!\n')
                break
        else:
            open('Transaction File.txt', 'a')
            while True:
                print('Do you wish to start a new transaction? [y]/[n]')
                choice = input('> ')
                if choice.lower() == 'y': 
                    inputFrom = user_string_input('Please enter your name, then press enter: ')
                    inputTo = user_string_input('Please enter the name of the recipient, then press enter: ')
                    inputAmount = user_int_input('Please enter the amount you wish to send, then press enter: ')
                    timestamp = date.datetime.now()
                    if os.path.getsize('Transaction File.txt') == 0:                  #(Quadri, M., (2015). 'How to check text file exists and is not empty in python'. StackOverflow. Retrieved from https://stackoverflow.com/questions/28737292/how-to-check-text-file-exists-and-is-not-empty-in-python/28737358)
                        index = 1
                    else:
                        with open('Transaction File.txt','r') as tf:
                            last_index = ((tf.readlines()[-5])[20:]).strip()
                            index = (int(last_index) + 1)
                    transaction = str('\nTransaction Number: '+ str(index) +
                                      '\nTimestamp: ' + str(timestamp) +
                                      '\nFrom: ' + inputFrom +
                                      '\nTo: ' + inputTo +
                                      '\nAmount: ' + str(inputAmount) + '\n')
                    print('\nRecording transaction...')
                    with open('Transaction File.txt', 'a') as tf:
                        tf.write(transaction)
                        tf.close()
                    print('\nTransaction saved.\n')
                    first_trans = False
                elif choice.lower() == 'n': 
                    print('Are you sure you want to return to the main menu? [y]/[n]')
                    choice = input('> ')
                    if choice.lower() == 'y':
                        break
                    elif choice.lower() == 'n':
                        continue
                    else:
                        print('Invalid choice. Please choose one of the given options.')
                        continue
                else:
                    print('Invalid choice. Please choose one of the given options.')
                    continue
                
                
                





























        
