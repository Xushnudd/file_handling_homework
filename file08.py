def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(f"data/{data}", 'r')
    text = f.read()
    a = 0
    for i in text:
        if i.isdigit():
            b = int(i)
            if b>a:
                a = b
    return a
# Read data from file
print(main("data08.txt"))