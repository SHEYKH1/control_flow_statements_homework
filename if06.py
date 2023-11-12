def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    s_p=0
    s_n=0
    if a>0:
        s_p=1
    if a<0:
        s_n+=1

    if b>0:
        s_p+=1
    if b<0:
        s_n+=1

    if c>0:
        s_p+=1
    if c<0:
        s_n+=1

    if s_p>s_n:
        return  "there are a lot of positive numbers"                    
    if s_p<s_n:
        return "there are a lot of negative numbers"
    print(main(3,-4,7))

