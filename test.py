import hashlib
import Config
import random
import Reduction

def get_check_digit(test):
    return 3

def get_seed():       
    seed = str(random.randint(0,999999999)).zfill(9)
    seed = str(Config.prefix)+seed
    seed= seed+str(get_check_digit(seed))
    return seed


start = get_seed()         
seed = start
    #THIS MIGHT NEED TO NOT BE 0!!!!!!!!!!!!!!!
for run in range(1,100):
    #reduce the hash   
    seed=Reduction.reduce(hashlib.sha256(str(seed)).hexdigest(),run) #@UndefinedVariable
    #print seed
print start, hashlib.sha256(str(seed)).hexdigest() #@UndefinedVariable