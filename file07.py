def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
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
            a += int(i)
    return a
# Read data from file
print(main("data07.txt"))