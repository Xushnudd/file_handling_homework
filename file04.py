def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(f"data/{data}", 'r')
    text = f.read()

    a = []

    for i in text:
        if i.isdigit() == False:
            a.append(i)
    return a

# Read data from file
print(main("data04.txt"))
# Read data from file