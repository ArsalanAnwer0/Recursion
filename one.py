# Recursion
# Direct Recursion
# Indirect Recursion

def printNumbers(Lrange,Urange):
    # Base range
    if Lrange > Urange:
        return
    
    print(Lrange)

    printNumbers(Lrange+1,Urange)


printNumbers(1,5)