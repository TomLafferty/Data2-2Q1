def fibonacci(fin: float) -> float:
    """
    build a classic fibonacci function - No RECURSION
    """
    a = 0
    b = 1
    # For n < 0 not valid
    if fin < 0:
        print('Invalid input.')

    # For n = 0 return 0
    elif fin == 0:
        return 0

    # For n = 1 or 2 return 1
    elif fin ==1:
        return 1

    # Else perform function
    else:
        for element in range(1, fin):
            c = a + b
            a = b
            b = c
        return b

    # pass  # implement me