def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(f"data/{data}", 'r')
    text = f.read()

    a = []

    for i in text:
        if i.isdigit():
            a.append(i)
    return a

# Read data from file
print(main("data03.txt"))