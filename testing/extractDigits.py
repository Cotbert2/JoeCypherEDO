def extractDigits(number):
    if(number < 10):
        number = str(int(number)) * 10
    elif (number>=10):
        number = int(str(number)[0:2])
    return number