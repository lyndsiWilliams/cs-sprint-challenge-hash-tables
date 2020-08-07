def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create a table to hold the weights
    weights_table = {}

    # Loop through the length parameter
    for i in range(length):
        # Check for duplicate values
        if weights[i] in weights_table:
            # Add the index of the duplicate to the value of the key
            weights_table[weights[i]].append(i)
        # Otherwise, it's not in the table yet so add it as a list item
        else:
            weights_table[weights[i]] = [i]

    # Loop through the keys in the weights_table
    for i in weights_table:
        # Set a variable to watch for the limit
        total = limit - i

        # If the calculated total exists in the weights_table...
        if total in weights_table:
            # Check for duplicate values
            if len(weights_table[total]) != 1:
                # Return the array containing the indices
                # and convert them into a tuple
                return tuple(sorted(weights_table[total], reverse=True))
            # Otherwise, calculate normally on one value
            else:
                # In order to get this tuple properly,
                # The first entry's value is accessed by the current key subtracted from the limit
                # The second entry is accessed by the current key
                # Then you reverse it so it's key/value
                return tuple(sorted((weights_table[total][0], weights_table[i][0]), reverse=True))

    # If there is no possible weight combination, return None
    return None
