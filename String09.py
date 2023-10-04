def main(s):
    """
    A str containing the letter "a" is given. Find the number of letters "a" in this variable.
    Args:
        s: str
    Returns:
        int: answer
    """ 
    a=0
    for i in s:
        if i=='a':
            a+=1
    return a
print(main('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))