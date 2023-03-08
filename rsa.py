import time

# Helper functions

def letters2digits(letters):
  digits = ""
  for c in letters:
    if c.isalpha():
      letter = c.upper()  #converting to uppercase
      d = ord(letter) - 65
      if d < 10:
        digits += "0" + str(d)  # concatenating to the string of digits
      else:
        digits += str(d)
  return digits

def digits2letters(digits):
  letters = ""
  start = 0  #initializing starting index of first digit
  while start <= len(digits) - 2:
    digit = digits[start:start + 2]  # accessing the double digit
    letters += chr(int(digit) + 65)  # concatenating to the string of letters
    start += 2  # updating the starting index for next digit
  return letters

def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2

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
  return abs(s * a + t * b)

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

# RSA 

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
      newBlock = str(mod_exp(int(c), e, n)) # RSA encryption function
      # make sure the new block has the len of blocksize
      newBlock = newBlock.zfill(size)
      # add this block to the list of encrypted blocks 
      encrypted.append(newBlock)
    # join the blocks together into a string 
    encryptedDigits = " ".join(encrypted)
    # return the result (encryptedDigits)
    return encryptedDigits

# test (see lecture 6 for examples)
# encryptRSA("STOP", 2537, 13) # works 
# encryptRSA("UPLOADS", 3233, 17) # works 
    
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
      # make sure the new block has the len of blocksize
      newBlock = newBlock.zfill(size)
      # add this block to the list of encrypted blocks 
      decrypted.append(newBlock)
    # join the blocks together into a string 
    decryptedDigits = "".join(decrypted)
    # convert digits into plaintext
    plaintext = digits2letters(decryptedDigits)
    return plaintext

"""--------------------- TESTER CELL ---------------------------"""
decrypted1 = decryptRSA("2081 2182", 43, 59, 13)
decrypted2 = decryptRSA("0981 0461", 43, 59, 13)
decrypted3 = decryptRSA("2081 2182 1346", 43, 59, 13)
print("Decrypted Message:", decrypted1)
print("Expected: STOP")
print("Decrypted Message:", decrypted2)
print("Expected: HELP")
print("Decrypted Message:", decrypted3)
print("Expected: STOPSX")

"""--------------------- TEST 2---------------------------"""
decrypted = decryptRSA("0667 1947 0671", 43, 59, 13)
print("Decrypted Message:", decrypted)
print("Expected: SILVER")