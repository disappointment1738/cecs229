# helper functions

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

def affineEncrypt(text, a, b):
  """encrypts the plaintext 'text', using an affine transformation key        (a, b)
    INPUT:  text - plaintext as a string of letters
            a - integer satisfying gcd(a, 26) = 1.  Raises error if such                  is not the case
            b - integer 
            
    OUTPUT: The encrypted message as a string of characters
    """
  # cannot make a key if the gcd(a, 26) != 1
  if int(gcd(a, 26)) != 1:
    raise ValueError("The given key is invalid. The gcd(a,26) must be 1.")
  # converting text to nums
  digits = letters2digits(text)
  encryDigits = ""
  # encrypting each number 
  for i in range(0, len(digits), 2):
    encryDig = str((a * int(digits[i:i + 2]) + b) % 26) # affine shift function
    if len(encryDig) == 1: # need to add a 0 in front of the digit if less than 10
        encryDigits += "0" + encryDig
    else:
        encryDigits += encryDig
  text = digits2letters(encryDigits) # convert back to letters
  return text

# tester
affineEncrypt("MEET YOU IN THE PARK", 1, 3)

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

# tester
affineDecrypt("PHHWBRXLQWKHSDUN", 1, 3)