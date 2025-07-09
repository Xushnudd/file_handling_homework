def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(f"data/{data}", 'r')
    return list(f.read())

# Read data from file
print(main("data02.txt"))