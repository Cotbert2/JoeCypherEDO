def extractDigits(number):
    number = abs(int(number))
    if number < 10:
        return number * 11
    elif number >= 100:
        return int(str(number)[:2])
    return number
