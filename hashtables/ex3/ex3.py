def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Set a dictionary for the numbers
    numbers = {}

    # Set a list for the result
    result = []

    # Loop through the length of the parameter arrays
    for i in range(len(arrays)):
        # Create a key and value for each array
        for j in arrays[i]:
            # If a duplicate is found for the current number, add to the count
            if j in numbers:
                numbers[j] += 1
            # Otherwise, this is the first occurence of this number so start the count
            else:
                numbers[j] = 1

    # Loop through the numbers dictionary
    for i in numbers:
        # Check if the current number exists in all of the arrays
        if numbers[i] == len(arrays):
            # If so, add it to the result list
            result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
