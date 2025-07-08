def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(f"data/{data}", 'r')
    text = f.read()
    a = "a"
    for i in text:
        if i.isdigit():
            b = int(i)
            if a=="a":
                a = b
            elif b<a:
                a = b
    return a
# Read data from file
print(main("data09.txt"))