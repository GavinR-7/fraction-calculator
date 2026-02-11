def getFractions():
    num1 = int(input("Enter the numerator of the first fraction: "))
    denom1 = int(input("Enter the denominator of the first fraction: "))
    num2 = int(input("Enter the numerator of the second fraction: "))
    denom2 = int(input("Enter the denominator of the second fraction: "))
    
    if denom1 ==0 or denom2 ==0:
        return None #or raise an error
    
    if (denom1 == denom2):
        return eqDenom(num1, denom1, num2, denom2)
    else:
        return diffDenom(num1, denom1, num2, denom2)

def eqDenom(num1, denom1, num2, denom2):
    finalNum = num1 + num2
    finalDenom = denom1
    return simplify(finalNum, finalDenom)

def diffDenom(num1, denom1, num2, denom2):
    finalDenom = denom1 * denom2
    finalNum = num1*denom2 + num2*denom1
    return simplify(finalNum, finalDenom)

def simplify(num, denom):
    i = 2
    while (i <= abs(num) and i <= abs(denom)):
        if (num % i == 0 and denom % i == 0):
            num //= i
            denom //= i
            i = 2
        else:
            i += 1
    return num, denom

print(getFractions())