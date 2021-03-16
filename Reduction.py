import CardTools
import Config
import string
import math

def reduce(hash, run):
    all=string.maketrans('','')    
    nochar=all.translate(all,string.digits)
    #get rid of non digits.
    account= int(str(Config.prefix)+hash.translate(all,nochar))
    
    #get cosign and truncate results to 9 characters
    reducto = str(abs(math.cos(account)*999999999*run))[:9]
    
    #add check digit to result.
    account=reducto+CardTools.get_check_digit(account)
    return account



