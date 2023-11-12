def main(a):
    """
     two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    Z=a%10
    X=a//10
    if Z<=X:
        return True
    return False
print(main(50))
print(main(23))