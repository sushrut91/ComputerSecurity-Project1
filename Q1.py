#!/usr/bin/python3
import math

def main():
    try:
        a = int(input("Enter the value of a: "))
        p = int(input("Enter the value of p: "))
        
        if a < 0 or p < 0:
            print ('Values of a and p should be greater than 0')
        else:
            mod_val = a % p           
            if a > p:
                print('Error..Value of a < p')
            else:
                if isPrime(p):
                    print('a mod p =', mod_val)
                    rev_mod = (a ** (p-2)) % p
                    print('Reverse modulus of of a is: ',rev_mod)
                    check_ans = (a * rev_mod) % p
                    print('Checking the answer a * a(inverse) = ({} * {}) % {} yields answer : {}'
                          .format( a, rev_mod, p,check_ans ))
                else:
                    print('p should be a prime number to calculate a inverse')
        
    except ValueError:
        print('Please enter valid integer values for a & p')
    except ZeroDivisionError:
        print('Please enter p > 0')
  

#Function to check if number is prime or not    
def isPrime(n):
    flag = True
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            flag = False
    return flag  
if __name__ == "__main__": main()