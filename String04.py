def main(s):
    """
    A variable of type str is given. make sure all letters are lowercase.
    Args:
        s: str
    Returns:
        bool: answer
    """
    w=s.lower()
    if w==s:
        return True
    if w!=s:
        return False
print(main('hello world'))