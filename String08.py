def main(s):
    """
    A variable of type str is given. Make sure it only consists of uppercase letters.
    Args:
        s: str
    Returns:
        bool: answer
    """
    w=s.upper()
    if w==s:
        return True
    if w!=s:
        return False
