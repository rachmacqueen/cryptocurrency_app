# Name: Rachel Sanders
# This application was created as an assignment for the Cryptographic Concepts unit, as part of Edith Cowan University's Y89 Bachelor of Science (Cyber Security)
# Python 3.6.5 was used for this assignment


# Import the required modules
import os                                                                               #allows for operating system procedures such as reading of file statistics
import time                                                                             #allows for the checking of a file every x amount of seconds
import datetime as date                                                                 #allows for creating a timestamp of the current date/time
from Crypto.Hash import SHA256                                                          #allows the use of the SHA256 hashing algorithm for encrypting data/blocks



#This class creates a new object called a Block with four parameters: index, time, data, and previous hash.
class Block:                                                                           #(Nash, G., (2017). ‘Let’s Build the Tiniest Blockchain in Less Than 50 Lines of Python’. Medium Corporation. Retrieved from https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b)
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.SHA_hash()
         
    def SHA_hash(self):                                                               #(Individual contributors., (2018). ‘SHA-256’. PyCryptodome. Retrieved from http://pycryptodome.readthedocs.io/en/latest/src/hash/sha256.html)
        h = SHA256.new()
        h.update((str(self.data)).encode())
        return h.hexdigest()
            
        
#This function creates a new block for the transaction data, then identifies the nonce which produces a hash including 14 zeros and updates the BlockChain file with the successful hash

def block_mining(last_index, last_hash, transaction):
    print('Creating a new block.')
    this_index = (int(last_index) + 1)
    next_block = Block(index = this_index,
                       timestamp = date.datetime.now(),
                       data = transaction,
                       previous_hash = last_hash)
    nonce = 0
    print('Please wait whilst the hash value of the new block is verified...')
    while True:      
        h = SHA256.new()
        h.update((str(next_block.previous_hash)+
                  str(next_block.data)+
                  str(nonce)).encode())
        nonce_hash = h.hexdigest()
                     
        if nonce_hash.count('0') == 14:             
            with open('BlockChain.txt', 'a') as bc:
                next_block.hash = nonce_hash
                bc.write('\nBlock #{}\n'.format(next_block.index)+
                         'Timestamp: {} \n'.format(next_block.timestamp)+
                         'Data: {} \n'.format(next_block.data)+
                         'Hash: {}\n'.format(next_block.hash)+
                         'Previous Hash: {}\n'.format(next_block.previous_hash))
                bc.close()
                print('The new block has been successfully added to the blockchain.\n')
                break
        elif nonce > 50000:                         
            with open('BlockChain.txt', 'a') as bc:
                next_block.hash = nonce_hash
                bc.write('\nBlock #{}\n'.format(next_block.index)+
                         'Timestamp: {} \n'.format(next_block.timestamp)+
                         'Data: {} \n'.format(next_block.data)+
                         'Hash: {}\n'.format(next_block.hash)+
                         'Previous Hash: {}\n'.format(next_block.previous_hash))
                bc.close()
                print('The new block has been successfully added to the blockchain.\n')
                break

        nonce += 1
        

#start of program

while True:
        first_trans = True
        new_tf = open('Transaction File.txt', 'w')
        new_tf.close()
        print('\nWelcome to the Block Mining Program! This application monitors the Transaction File for changes and chains any new transactions to the existing block chain! \nPlease press any key to begin, or else press [q] to quit.')
        choice = input('> ')
        if choice.lower() == 'q':
            print('\nFarewell!\n')
            break
        else:
            while True:               
                with open('BlockChain.txt', 'a+') as bc:                 #creating the BlockChain file/opening the existing BlockChain file
                    if 'Hash' not in open('BlockChain.txt').read():     #checking if any previous blocks exist - if not, the first block is formed
                        print('Creating a new BlockChain file.\n')
                        blockchain = Block(index=0,
                                           timestamp=date.datetime.now(),
                                           data='first block',
                                           previous_hash='0')
                        last_block = blockchain
                        bc.write('Block #{}\n'.format(blockchain.index)+
                                 'Timestamp: {} \n'.format(blockchain.timestamp)+
                                 'Data: {} \n'.format(blockchain.data)+
                                 'Hash: {}\n'.format(blockchain.hash)+
                                 'Previous Hash: {}\n'.format(blockchain.previous_hash))
                        bc.close()

                #checking if the has any data in it - if not, prompt for TRP use
                if os.path.getsize('Transaction File.txt') == 0:                                    #(Quadri, M., (2015). 'How to check text file exists and is not empty in python'. StackOverflow. Retrieved from https://stackoverflow.com/questions/28737292/how-to-check-text-file-exists-and-is-not-empty-in-python/28737358)
                    print('There are currently no transactions in the Transaction File. Please use the TRP program to add a new transaction.')
                    first_trans = True
                    break

                with open('Transaction File.txt', 'r') as tf:
                    last_trans = ((tf.readlines()[-5])[20:]).strip()            #returns just the number of the last transaction
                    tf.close()
                    print('Checking for updates to the Transaction File... (Press [q] to quit to the main menu or ENTER to continue)')
                    choice = input('> ')
                    if choice.lower() == 'q':
                        break
                    else:
                        timer = time.time()
                        while True:
                            with open('Transaction File.txt', 'r')as rtf:
                                current_trans = ((rtf.readlines()[-5])[20:]).strip()
                                if current_trans == last_trans and first_trans is False:        #checking if the transaction numbers match or it's not the first transaction - if not, the next block is created
                                    print('There are currently no new transactions. The file will be checked again in 15 seconds.\n')
                                    time.sleep(15 - time.time() % 15)                                               #(Rove, D., (2014). ‘What is the best way to repeatedly execute a function every x seconds in Python?’. StackOverflow. Retrieved from https://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds-in-python)
                                    continue
                                else:
                                    print('New transaction found - proceeding with block creation.')
                                    with open('BlockChain.txt', 'r') as rbc, open('Transaction File.txt', 'r') as rtf:
                                        rbc_lines = rbc.readlines()
                                        rtf_lines = rtf.readlines()
                                        data = rtf_lines[-3:]
                                        transaction = str([s.replace('\n', '') for s in data])                      #(Ritzel, J., (2011). ‘Removing character in a list of strings’. StackOverflow. Retrieved from https://stackoverflow.com/questions/8282553/removing-character-in-list-of-strings)print('New transaction found - proceeding with block creation.')
                                        last_index = ((rbc_lines[-5])[7:]).strip()
                                        last_hash = ((rbc_lines[-2])[6:]).strip()
                                    block_mining(last_index, last_hash, transaction)
                                    first_trans = False
                                    break                   
                                
                
                
                    
                    
                    


                
                
























        
