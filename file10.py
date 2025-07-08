def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(f"data/{data}", 'r')
    text = f.readlines()
    a = 0
    for i in text:
        b = len(i.strip())
        if b>a:
            a+=b
    return a
# Read data from file
print(main("data10.txt"))