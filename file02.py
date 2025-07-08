def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(f"data/{data}", 'r')
    return len(f.read())

# Read data from file
print(main("data02.txt"))