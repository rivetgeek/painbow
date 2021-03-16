import Config 
import random
import hashlib     
import Reduction  

def get_check_digit(ccnumber):
    sum = 0
    pos = 0
    length = 16
    ccnumber=str(ccnumber)
    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()

    while pos < length - 1:

        odd = int( reversedCCnumber[pos] ) * 2
        if odd > 9:
            odd -= 9

        sum += odd

        if pos != (length - 2):

            sum += int( reversedCCnumber[pos+1] )

        pos += 2
    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10
    return str(checkdigit)

def get_seed():       
    seed = str(random.randint(0,999999999)).zfill(9)
    seed = str(Config.prefix)+seed
    seed= seed+str(get_check_digit(seed))
    return seed


def create_chain():
    start = get_seed()        
    seed = start
        #THIS MIGHT NEED TO NOT BE 0!!!!!!!!!!!!!!!
    for run in range(1,Config.chain_length):
        #reduce the hash   
        seed=str(Config.prefix)+str(Reduction.reduce(hashlib.sha256(str(seed)).hexdigest(),run)) #@UndefinedVariable

    return start, hashlib.sha256(str(seed)).hexdigest() #@UndefinedVariable
    
    
    