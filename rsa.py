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

# RSA 

def encryptRSA(message, n, e):
    """encrypts the plaintext message, using RSA and the key (n = p * q, e)
    INPUT:  message - plaintext as a string of letters
            n - a positive integer
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The encrypted message as a string of digits
    """
    # todo
    pass
    
def decryptRSA(cipher, p, q, e):
    """decrypts cipher, which was encrypted using the key (p * q, e)
    INPUT:  cipher - ciphertext as a string of digits
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The decrypted message as a string of letters
    """
    # todo
    pass

