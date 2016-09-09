#!/usr/bin/python3
from _ctypes import FormatError
def main():
    try:
        n1 = int(input('Enter an integer: '))
        n2 = int(input('Enter an integer: '))
        if n1 == 0 or n2 == 0:
            print('Enter n1 and n2 both should be greater than 0')
            return -1 # Return error
        else:
            gcd = GCD(n1,n2)
            print('\nThe G.C.D of {} and {} is {}'.format(n1, n2, gcd))
            return 0
            
    except ValueError:
        print('You entered a non integer value. Please try again.')

#Function which returns GCD of both values            
def GCD(n1,n2):
    # Convert negative values to positive values
    if n1 < 0:
        n1 = -n1
    if n2 < 0:
        n2 = -n2
    #Ensure that n2 is always greater

    if n2 > n1:
        temp = n1
        n1 = n2
        n2 = temp
    r=1
    #Euclid's algorithm
    while r > 0:
        r = n1 % n2
        if r == 0:
            return n2
        n1 = n2
        n2 = r    
        
         
if __name__ =='__main__': main()