def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for i, j in a_dictionary.items():
            if j == value:
                del a_dictionary[k]
                break

    return (a_dictionary)
