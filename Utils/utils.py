def read_input(infile):
    """Reads a .txt input file and returns the data.

    Args:
        infile (str): .txt file of multiple lines

    Returns:
        list: list of lines from input file (str)
    """
    from os import getcwd

    with open(f'{getcwd()}/input.txt', 'r') as infile:
        data = infile.read().splitlines()

    return data