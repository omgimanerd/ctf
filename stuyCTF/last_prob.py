#!/usr/bin/python2.7
import math

double_numbers = [3570793128, 1458104314, 3260858022, 1345134392, 749597442, 289067508, 2759917644, 181602112, 1449980724, 1535408668, 988033496, 1457695096, 1802710596, 2496283884, 34647282, 2272064548, 3969791992, 2236522198, 2371091990, 3947054260, 338067104, 4274799248, 101450696]
double_numbers = double_numbers[::-1]
print double_numbers
length = 23

def roots(a, b, c):

    def getDiscriminant(a, b, c):
            return (b ** 2 - (4 * a * c)) ** .5

    D = getDiscriminant(a, b, c) 

    b = -b
    a = 2 * a

    firstroot = float((b + D) / float(a))
    secondroot = float((b - D) / float(a))

    return firstroot


def solver (ans, length, pot):
        for i in range(1,(length - 1)):
                ans = roots(1, (-1*ans*(pot[i+1])),(pot[i])*(pot[i+1]))
                print ans
        return ans

print solver(5362426, 23, double_numbers)
