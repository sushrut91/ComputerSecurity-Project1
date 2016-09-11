#!/usr/bin/python3
import re

def main():
    # Letters set a-z and space
    letters = {'a':0, 'b':1, 'c':2 , 'd':3 , 'e':4, 'f':5 , 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 
               'o':14, 'p':15 , 'q':16 , 'r':17, 's':18 , 't':19 , 'u':20, 'v':21, 'w':22 , 'x':23, 'y':24 , 'z':25,' ':26}
    
    #Input letters for the program    
    input_string = input('Enter a string to encrypt containing (a-z) and space : ')
    
    if re.match('^[a-z ]*$', input_string, 0) is None:
        print('Illegal characters entered. Small case alphabets (a-z) and space are only allowed characters. Please rerun the program.')
        return -1
    
    print('[a,b,c,d] will be your 2x2 matrix of keys used :')
    a = input('Enter the value of a : ')
    b = input('Enter the value of b : ')
    c = input('Enter the value of c : ')
    d = input('Enter the value of d : ')
    
    if re.match('^-?[0-9]*$',a,0) is None or re.match('^-?[0-9]*$',b,0) is None or re.match('^-?[0-9]*$',c,0) is None or re.match('^-?[0-9]*$',d,0) is None:
        print('Only numeric integer values allowed. Enter an integer having digits 0-9. Please rerun the program.')
        return -1
    
    #Append a space if there are odd no of characters
    if not len(input_string) % 2 == 0:
        input_string = input_string + ' '
    a,b,c,d = int(a),int(b),int(c),int(d)    
    #a , b , c, d = 3,2,4,7
    
    cipher_text = EncyptDiagraph(a,b,c,d,input_string,letters)
    print('****Diagraph Encryption****\n')
    print('Encrypted message : ',cipher_text)
    print('KEYS: (a : {} , b: {}, c: {}, d: {})'.format(a,b,c,d))
    plain_text = DecryptDiagraph(a, b, c, d, cipher_text, letters)
    print('Decrypted message : ',plain_text)

#Decrypt the encypted string    
def DecryptDiagraph(a,b,c,d,cipher_string,letters):
    #inverting matrix, find modulur inverse
    n = len(letters)
    determinent = (a * d) - (b * c)
    if determinent == 0 :
        return 'Determinent value of matrix was found to be 0. Please retry using new values for keys.'
    else:
        x=1
        while True:
            if (determinent * x) % n  == 1 :
                break
            if x> determinent+500:
                return 'Error calculating modular inverse as this leads to infinite loops. Please retry with new smaller values.'
            x = x + 1
            
        a , d = d * x,  a * x
        b = -b * x
        c = -c * x
        
        a_dash = a % n
        b_dash = b % n
        c_dash = c % n
        d_dash = d % n
          
        i = 0
        decrypt_chars = list()
        plaintext = ''
        while i < (len(cipher_string)-1):
            p1 = ((a_dash * letters.get(cipher_string[i])) + (b_dash * letters.get(cipher_string[i+1]))) % len(letters)
            p2 = ((c_dash * letters.get(cipher_string[i])) + (d_dash * letters.get(cipher_string[i+1]))) % len(letters)
            decrypt_chars.append(p1)
            decrypt_chars.append(p2)       
            i = i + 2
        # Decrypt pairs of characters
        for num in decrypt_chars:
            for key,value in letters.items():
                if num == value:
                    plaintext = plaintext + str(key)
        return plaintext
    
        
            
def EncyptDiagraph(a,b,c,d,input_string, letters):
    i = 0
    encrypt_chars = list()
    ciphertext = ''
    while i < (len(input_string)-1):
        c1 = ((a * letters.get(input_string[i])) + (b * letters.get(input_string[i+1]))) % len(letters)
        c2 = ((c * letters.get(input_string[i])) + (d * letters.get(input_string[i+1]))) % len(letters)
        encrypt_chars.append(c1)
        encrypt_chars.append(c2)       
        i = i + 2
    # Encrypt pairs of characters
    for num in encrypt_chars:
        for key,value in letters.items():
            if num == value:
                ciphertext = ciphertext + str(key)
    return ciphertext
if __name__ == "__main__" : main()