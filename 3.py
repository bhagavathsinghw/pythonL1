import string  
def find_e(x):
    if x.count('e') == 2:
        return True
    else:
        return False

try:
    x=raw_input("Enter String :")
    print find_e(x)
except:
    print "Error"