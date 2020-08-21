# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Set a dictionary for the files
    files_dict = {}

    # Set a dictionary for the queries
    queries_dict = {}

    # Set a list for the result
    result = []

    # Loop through the parameter files
    for i in files:
        # Set a space in the dictionary for each entry
        files_dict[i] = None

    # Loop through the parameter queries
    for i in queries:
        # Set a space in the dictionary for each entry
        queries_dict[i] = None

    # Loop through the files dictionary
    for i in files_dict:
        # Split the file into searchable "words"
        words = i.split("/")[-1]

        # If one of the file's "words" are found in the queries_dict
        if words in queries_dict:
            # Add it to the result list
            result.append(i)

    # Return the matched query
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
