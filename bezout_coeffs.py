def bezout_coeffs(a, b):
    """that computes the Bezout coefficients s and t of a and b.
    param@ int a
    param@ int b
    """
    # save values for later
    x, y = a, b
    # gcd( |a|, |b| ) = gcd(a, b) for any integers a and b (positive or negative)
    if a < 0:
        a = (-1) * a
    if b < 0:
        b = (-1) * b
    # declaration of variables
    s, s1 = 1, 0 # coeffs for a
    t, t1 = 0, 1 # coeffs for b
    r, r1 = a, b # remainders
    q = r // r1 # quotient
    
    while r1 != 0:
        q = r // r1
        # Swapping variables without creating temp variable
        # Now r1 = r and r = r1 - q*r , &  s1 = s and s = s1 - q*s1 , & t = t1 and t1 = t - q * t1
        r, r1 = r1, r - q * r1
        s, s1 = s1, s - q * s1
        t, t1 = t1, t - q * t1
    # create dictionary for bezout coeffs
    bezout = {x: s, y: t} # where x is the original a and y is the original b
    return bezout

bezout_coeffs(414, 662)
print('expected {414 : 8, 662 : -5}')