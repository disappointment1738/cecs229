#!/usr/bin/env python
# coding: utf-8

# # CECS 229 Programming Assignment #3
# 
# #### Due Date: 
# 
# Sunday, 3/5 @ 11:59 PM
# 
# #### EXTENDED UNTIL 3/7 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit to CodePost this file converted to a Python script named `pa3.py`
# 
# #### Objectives:
# 
# 1. Find the inverse of a given integer under a given modulo m.
# 2. Encrypt and decrypt text using an affine transformation.
# 3. Encrypt and decrypt text using the RSA cryptosystem.
# 
# 
# 
# 
# ### Programming Tasks
# 
# You may use the utility functions at the end of this notebook to aid you in the implementation of the following tasks.

# 
# ### Helper Functions:
# 
# These functions are from past PAs, used to help with PA3.
# 
# Functions used:
# 1. `mod_exp(b, n, m)`
# 2. `bezout_coeffs(a, b)`
# 3. `gcd(a, b)`

# In[ ]:


def mod_exp(b, n, m):
    """
    this function computes b^n mod m
    param@ base (b), exponent (n), modulo (m)
    returns an int as result
    """
    if b < 0 or n < 0 or m < 0:
        return 0
    nBinary = bin(n)[2:]
    x = 1
    p = b % m
    for i in range(len(nBinary)-1, -1, -1):
        if int(nBinary[i]) == 1:
            x = (x * p) % m 
        p = (p * p) % m
    return x


# In[ ]:


def bezout_coeffs(a, b):
    """that computes the Bezout coefficients s and t of a and b.
    param@ int a
    param@ int b
    """
    x, y = a, b
    if a < 0:
        a = (-1) * a
    if b < 0:
        b = (-1) * b
    s, s1 = 1, 0
    t, t1 = 0, 1
    r, r1 = a, b
    q = r // r1
    
    while r1 != 0:
        q = r // r1
        r, r1 = r1, r - q * r1
        s, s1 = s1, s - q * s1
        t, t1 = t1, t - q * t1
    bezout = {x: s, y: t}
    return bezout


# In[ ]:


def gcd(a, b):
    """
    computes the greatest common divisor of a and b using the bezout_coeff
    param@: int a and b
    """
    if b == 0:
        return abs(a)
    bezout = bezout_coeffs(a, b)
    s = bezout.get(a)
    t = bezout.get(b)
    return abs(s*a + t*b)


# ------------------------------------------
# #### Utility functions (NO EDITS NECESSARY)

# In[ ]:


def digits2letters(digits):
    letters = ""
    start = 0  #initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start : start + 2]  # accessing the double digit
        letters += chr( int(digit) +65)   # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters


# In[ ]:


def letters2digits(letters):
    digits = ""
    for c in letters:
        if c.isalpha():
            letter = c.upper()  #converting to uppercase  
            d = ord(letter)-65
            if d < 10:
                digits += "0" + str(d)     # concatenating to the string of digits
            else:
                digits += str(d)
    return digits


# In[ ]:


def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2


# -------------------------------------------
# 
# #### Problem 1: 
# Create a function `modinv(a,m)` that returns the smallest, positive inverse of `a` modulo `m`.  If the gcd of `a` and `m` is not 1, then you must raise a `ValueError` with message `"The given values are not relatively prime"`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `pa3.py` file.

# In[ ]:


def modinv(a, m):
    """returns the smallest, positive inverse of a modulo m
    INPUT: a - integer
           m - positive integer
    OUTPUT: an integer in the range [0, m-1]
    """
    # if gcd(a, m) != 1, then the inverse does not exist.
    if gcd(a, m) != 1:
        raise ValueError("The given values are not relatively prime")
    # uses bezout_coeffs to find the inverse. the inverse is the bezout coeff of a
    inverse = bezout_coeffs(a, m).get(a)
    # checks if the inverse is in the range
    if inverse < 0:
        inverse += m
    if inverse >= m:
        # if the inverse is a lot bigger than (m-1), then we have to keep subtracting m until we're in range
        while inverse >= m: 
            inverse -= m
    return inverse


# In[ ]:


# TEST CASES, ALL WORK :)
# print(f'test case: mod(3, 7) -- returns {modinv(3,7)}. Expected 5')
# print(f'test case: mod(101, 4620) -- returns {modinv(101, 4620)}. Expected 1601')
# print(f'test case: mod(13, 2436) -- returns {modinv(13, 2436)}. Expected 937')
# print(f'test case: mod(3, 6) -- returns {modinv(3, 6)}. Expected "The given values are not relatively prime."')


# ------------------------------------
# 
# #### Problem 2: 
# Create a function `affineEncrypt(text, a,b)` that returns the cipher text encrypted using key  (`a`, `b`).  You must verify that the gcd(a, 26) = 1 before making the encryption.  If this is not the case, the function must raise a `ValueError` with message `"The given key is invalid. The gcd(a,26) must be 1."`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `pa3.py` file.

# In[ ]:


def affineEncrypt(text, a, b):
    """encrypts the plaintext 'text', using an affine transformation key (a, b)
    INPUT:  text - plaintext as a string of letters
            a - integer satisfying gcd(a, 26) = 1.  Raises error if such is not the case
            b - integer 
            
    OUTPUT: The encrypted message as a string of characters
    """
    # cannot make a key if the gcd(a, 26) != 1
    if int(gcd(a, 26)) != 1:
        raise ValueError("The given key is invalid. The gcd(a,26) must be 1.")
      # converting text to nums
    digits = letters2digits(text)
    encryDigits = "" # all of the digits 
      # encrypting each number 
    for i in range(0, len(digits), 2):
        digit = str((a * int(digits[i:i + 2]) + b) % 26) # affine shift function
        if len(digit) == 1: # need to add a 0 in front of the digit if less than 10
            encryDigits += "0" + digit
        else:
            encryDigits += digit
    text = digits2letters(encryDigits) # convert back to letters
    return text


# In[ ]:


# TEST CASES
# affineEncrypt("MEET YOU IN THE PARK", 1, 3)


# #### Problem 3: 
# Create a function `affineDecrypt(ciphertext, a,b)` that returns the cipher text encrypted using key  (`a`, `b`). You must verify that the gcd(a, 26) = 1.  If this is not the case, the function must raise `ValueError` with message `"The given key is invalid. The gcd(a,26) must be 1."`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `pa3.py` file.

# In[ ]:


def affineDecrypt(ciphertext, a, b):
    """decrypts the string 'ciphertext', which was encrypted using an affine transformation key (a, b)
    INPUT:  ciphertext - a string of encrypted letters
            a - integer satisfying gcd(a, 26) = 1.  
            b - integer 
            
    OUTPUT: The decrypted message as a string of characters
    """
    # cannot make a key if the gcd(a, 26) != 1
    if int(gcd(a, 26)) != 1:
        raise ValueError("The given key is invalid. The gcd(a,26) must be 1.")
    # converting text to nums
    digits = letters2digits(ciphertext)
    decryDigits = ""
    # encrypting each number 
    for i in range(0, len(digits), 2):
        digit = str(modinv(a, 26) * (int(digits[i:i + 2]) - b) % 26) # affine decryption function
        if len(digit) == 1: # need to add a 0 in front of the digit if less than 10
            decryDigits += "0" + digit
        else:
            decryDigits += digit
    text = digits2letters(decryDigits) # convert back to letters
    return text


# In[ ]:


# test case
# affineDecrypt("PHHWBRXLQWKHSDUN", 1, 3)


# -----------------------------------
# 
# #### Problem 4:
# 
# Implement the function `encryptRSA(message, n, e)` which encrypts a string `message` using RSA key `(n = p * q, e)`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented for previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `pa3.py` file.

# In[ ]:


def encryptRSA(message, n, e):
    """encrypts the plaintext message, using RSA and the key (n = p * q, e)
    INPUT:  message - plaintext as a string of letters
            n - a positive integer
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The encrypted message as a string of digits
    """
    # find the blocksize, size
    size = blocksize(n)
    # create a list of the blocks and for encrypted blocks
    blocks = []
    encrypted = []
    # convert text to digits
    digits = letters2digits(message)
    # when len(digits) doesn't divide size, then we need to pad the message with "X" (or "23")
    while len(digits) % size != 0:
      digits += "23"
    # seperate the message into the blocksize
    for i in range(0, len(digits), size):
      blocks.append(digits[i:i+size])
    # now we want to encrypt every block
    for c in blocks:
      newBlock = str(mod_exp(int(c), e, n)) # # RSA encryption function
      # make sure the new block has the len of size
      while len(newBlock) < size:
        newBlock = "0" + newBlock
      # add this block to the list of encrypted blocks 
      encrypted.append(newBlock)
    # join the blocks together into a string 
    encryptedDigits = " ".join(encrypted)
    # return the result (encryptedDigits)
    return encryptedDigits


# In[ ]:


# """--------------------- ENCRYPTION TESTER CELL ---------------------------"""
# encrypted1 = encryptRSA("STOP", 2537, 13)
# encrypted2 = encryptRSA("HELP", 2537, 13)
# encrypted3 = encryptRSA("STOPS", 2537, 13)
# print("Encrypted Message:", encrypted1)
# print("Expected: 2081 2182")
# print("Encrypted Message:", encrypted2)
# print("Expected: 0981 0461")
# print("Encrypted Message:", encrypted3)
# print("Expected: 2081 2182 1346")


# """--------------------- TEST 2 ---------------------------"""
# encrypted = encryptRSA("UPLOAD", 3233, 17)
# print("Encrypted Message:", encrypted)
# print("Expected: 2545 2757 1211")

# # ALL WORK! :D


# -------------------------------------------------------
# 
# #### Problem 5:
# 
# Complete the implementation of the function `decryptRSA(c, p, q, m)` which depends on `modinv(a,m)` and the given functions `digits2letters(digits)` and `blockSize(n)`.  When you are done, you can test your function against the given examples.

# In[ ]:


def decryptRSA(cipher, p, q, e):
    """decrypts cipher, which was encrypted using the key (p * q, e)
    INPUT:  cipher - ciphertext as a string of digits
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The decrypted message as a string of letters
    """
    # find the inverse where e-bar is the inverse of e mod (p-1)(q-1)
    inverse = modinv(e, (p-1)*(q-1))
    # get rid of spaces in cipher
    cipher = cipher.replace(" ","")
    # find the blocksize, size
    size = blocksize(p*q)
    # create a list of the blocks and for encrypted blocks
    blocks = []
    decrypted = []
    # when len(cipher) doesn't divide size, then we need to pad the message with "X" (or "23")
    while len(cipher) % size != 0:
      cipher += "23"
    # seperate the message into the blocksize
    for i in range(0, len(cipher), size):
      blocks.append(cipher[i:i+size])
    # now we want to encrypt every block
    for c in blocks:
      newBlock = str(mod_exp(int(c), inverse, p*q)) # RSA decryption function
      # make sure the new block has the len of size
      while len(newBlock) < size:
        newBlock = "0" + newBlock
      # add this block to the list of encrypted blocks 
      decrypted.append(newBlock)
    # join the blocks together into a string 
    decryptedDigits = "".join(decrypted)
    # convert digits into plaintext
    plaintext = digits2letters(decryptedDigits)
    return plaintext


# In[ ]:


# """--------------------- TESTER CELL ---------------------------"""
# decrypted1 = decryptRSA("2081 2182", 43, 59, 13)
# decrypted2 = decryptRSA("0981 0461", 43, 59, 13)
# decrypted3 = decryptRSA("2081 2182 1346", 43, 59, 13)
# print("Decrypted Message:", decrypted1)
# print("Expected: STOP")
# print("Decrypted Message:", decrypted2)
# print("Expected: HELP")
# print("Decrypted Message:", decrypted3)
# print("Expected: STOPSX")

# """--------------------- TEST 2---------------------------"""
# decrypted = decryptRSA("0667 1947 0671", 43, 59, 13)
# print("Decrypted Message:", decrypted)
# print("Expected: SILVER")

# # works in vscode

