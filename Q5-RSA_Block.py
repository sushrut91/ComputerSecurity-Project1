#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():

    str = input('Enter a message : ')
   
    try:
        e = int(input('Enter a value for e(public key): '))
        p = int(input('Enter a prime no: '))
        q = int(input('Enter another prime no: '))
        
        if p == q:
            print('Both prime numbers should be different values')
            return -1
        if p * q < 127:
            print('Enter p and q values such that p * q > 127. Because 8bit unicode values used. This is done to prevent errors in decryption')
            return -1
        
        if IsPrime(p) and IsPrime(q): 
            cipher_text = list()
            plain_text = list()
        
            for c in str:
                cipher_char = EncryptCharRSA(c, p, q ,e)
                if cipher_char is not -1:
                    cipher_text.append(cipher_char)
                else:
                    break
            if cipher_char is not -1:
                for x in cipher_text:
                    plain_char,d,n = DecryptCharRSA(x, p, q, e)    
                    plain_text.append(plain_char)
            
                print ('\nOriginal Message: ', str)
                print ('\nPublic key used for encyption [e,n] : [{},{}]'.format(e,n))
                print ('\nEncrypted Message(UTF-8 Unicode characters) : ', end='')
                for element in cipher_text:
                    print(chr(element),end = '')
                
                print ('\nPrivate key used for decryption [d,n] : [{},{}]'.format(d,n))    
                print ('\n\nDecrypted Message: ', end='')
                
                for element in plain_text:
                    print(element,end='')
        else:
            print('Please enter only prime numbers:')
    except ValueError:
        print('Only integer values allowed')
        
def EncryptCharRSA(msg , p, q, e):
    n = p * q 
    phi = (p-1) * (q-1) 
    co_test = GCD(n, e)
    co_test_1 = GCD(phi,e)
     
    if co_test == 1 and co_test_1 == 1 and e<phi:                  
        cipher_no = 0
            
        for c in msg:
            cipher_no = (ord(c)** e) % n
            return cipher_no
    else:
        print('\n\ne:{} is not co-prime with n:{} and phi(n):{}. Choose another d value and retry'.format(e,n,phi))
        return -1
    
def DecryptCharRSA(msg,p, q,e):
    n = p * q
    phi = (p-1) * (q-1)
    d = ModularMultiplicativeInverse(e,phi)
    plain_no = (msg ** d) % n
    return chr(plain_no),d,n
    
def GCD(n1,n2):
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
              
    
# Get modular multiplicative inverse
def ModularMultiplicativeInverse(d,n):
    i = 1
    while True:
        if (d * i) % n == 1:
            return i
        i = i + 1
# Check if no is prime or not.
def IsPrime(n):
    flag = True
    for i in range(2,n):
        if n % i == 0:
            flag = False
        else:
            flag = True
    return flag
        
if __name__ == '__main__' : main()