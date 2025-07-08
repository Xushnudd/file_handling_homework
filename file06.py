def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(f"data/{data}", 'r')
    text = f.readlines()
    a = []
    for i in text:
        a.append(len(i.strip()))
    return a
# Read data from file
print(main("data06.txt"))