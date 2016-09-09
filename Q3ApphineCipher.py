#!/usr/bin/python3
import re
def main():
    letters = {'a':0, 'b':1, 'c':2 , 'd':3 , 'e':4, 'f':5 , 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 
               'o':14, 'p':15 , 'q':16 , 'r':17, 's':18 , 't':19 , 'u':20, 'v':21, 'w':22 , 'x':23, 'y':24 , 'z':25,' ':26}
    #a is the key and b denotes the shift taking place
    a ,b = 5,8
    
    input_string = input('Enter a string to encrypt containing alphabets.\nNumbers and special characters are not allowed. \nSpace is allowed: ')
    match_val = re.match("^[a-zA-Z ]*$", input_string, 0)
    
    try:
        a = int(input('Enter key1 (a): '))
        b = int(input('Enter key2 (b): '))
        if match_val is not None:
            cipher_string,decrypted_plain_string = '',''
            
            if AreRelativePrime(a, len(letters)):
                for letter in input_string:
                    cipher_string = cipher_string + EncryptCharacter(letter, letters, a, b) 
                        
                print ('Encrypted string : ', cipher_string)      
                
                for c_letter in cipher_string:
                    decrypted_plain_string = decrypted_plain_string + DecryptCharacter(c_letter, letters, a, b)           
                print('Value of a :' ,a)
                print('Value of b :' ,b)
                print ('Decrypted original string :', decrypted_plain_string)
            else:
                print('a and n, i.e length of charset should be co-prime numbers')
        else:
            print('You entered a invalid character')
    except ValueError:
        print('Only integer values are allowed')   
           
#Function to decrypt the characters
def DecryptCharacter(encrypt_char, letter_set, a, b):
    #P = a'(x)-b mod p
    #a' = a^(p-2) mod n
    n = len(letter_set)
    plain_char = encrypt_char
    encrypt_char_num = letter_set[encrypt_char]
 
    a_inverse = getModularInverse(a, n)
    plain_char = (a_inverse * (encrypt_char_num - b)) %n
        
        #Find the key from value 
    for key,value in letter_set.items():
        if value == plain_char:
            return str(key)
        
#Function to encrypt an input character     
def EncryptCharacter(plain_char, letter_set,a,b):
    # E(x) = (a(x) + b) mod p where a and p should be co-prime
    x = letter_set.get(plain_char)
    n = len(letter_set)
    cipher_char = plain_char
    
    if AreRelativePrime(a,n):
        cipher_char = (a*x + b) % n 
        for key,value in letter_set.items():
            if value == cipher_char:
                return str(key)
        
def AreRelativePrime(n1,n2):
# Numbers are relative prime if their GCD is 1, Euclid's algorithm
# Ensure n1 is always greater
# Ensure that n1 is always prime
    flag = True
    if n1 == n2:
        print('a and be cannot be equal.')
        return False
        
    if flag:
        if n2 > n1 :
            swap = n2
            n2 = n1
            n1 = swap
        remainder = n1
        while n2 > 1:
            remainder = n1 % n2
            n1 = n2
            n2 = remainder
        if remainder == 1:
            return True
        else:
            return False
    else:
        return False

#Calculate multiplicative inverse       
def getModularInverse(a,m):
    x=1
    while True:
        if (a * x) % m == 1  :
            break
        x=x+1
    return x
    
#Run the function main() at startup of the script    
if __name__ == "__main__": main()