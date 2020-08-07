def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Set a dictionary for the numbers
    numbers = {}

    # Set a list for the result
    result = []

    # Loop through the parameter list
    for i in a:
        # If the absolute value of the current number already exists
        # in the numbers dict, append it to the result list
        if abs(i) in numbers:
            result.append(abs(i))
        # Otherwise this value doesn't exist yet, so add it to the dict
        else:
            numbers[abs(i)] = 1

    # Return the resulting list
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
