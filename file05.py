def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(f"data/{data}", 'r')
    text = f.read()

    a = 0
    b = 0

    for i in text:
        if i.isdigit() == False:
            a += 1
        else:
            b += 1
    return [b, a]
print(main("data05.txt"))
    
# Read data from file