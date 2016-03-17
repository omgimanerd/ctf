#! /usr/bin/python

year = 2016

def daysInMonth(m):
    if m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        return 29
    else:
        return 31

def sumDigits(n):
    if n < 10:
        return n
    return n % 10 + sumDigits(n / 10)

def isPerfectPower(n, p):
    return n == int(round(n ** (1.0 / p))) ** p

total = 0
for month in range(1, 13):
    for day in range(1, daysInMonth(month) + 1):
        n = sumDigits(day) + sumDigits(month) + sumDigits(year)

        if not (isPerfectPower(n, 2) or isPerfectPower(n, 3)) and not (month == 12 and day == 25):
            total += n

print total

    
                
    
