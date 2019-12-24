
def checkTrucatablePrime(input,length):
    if length>2:
        if isPrime(input):
            input= truncateDigits(input,length)
            return checkTrucatablePrime(input,length-2)
        else:
            return False
    else:
        return isPrime(input)


def checkZeroOrLenghth(inputNumber):
    temp = inputNumber 
    cnt = 0
    while (temp != 0) : 
        cnt=cnt + 1 
        temp1 = temp % 10;  
        if (temp1 == 0) : 
            return True 
        temp = temp // 10
    return cnt

def truncateDigits(inputNumber,length):
    inputNumber = ((inputNumber // 10) % (10 ** (length-2)))
    return inputNumber

def isPrime(number):
    result = True
    if number<=1:
        result = False
    else :
        if number<=3:
            result = True
        else :
            if ((number % 2 ==0) or (number % 3 ==0)):
                result = False
            else:
                i = 5
                while(i * i <= number) : 
                    if (number % i == 0 or number % (i + 2) == 0):
                        result= False
                        break
                    i = i + 6
    
    return result