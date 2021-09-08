# adding values to keys is the start of the slides

w_freq = {
    'bzn': [1, 3, 4, 8, 10],
    'bil': [3, 10, 15, 7, 9],
    'mso': [5, 3, 7, 8, 1],
    'glf': [2, 3, 5, 6, 11],
    'hln': [10, 3, 9, 8, 12]
}

val_list = w_freq['bil']
print('values of key "bil" are: ')
print(val_list)


def add_values_in_dict(sample_dict, key, list_of_values):
    """append multiple values to a key in the given dictionary"""
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


a_freq = add_values_in_dict(w_freq, 'mso', [90, 93, 95])  # adding to existing key
b_freq = add_values_in_dict(w_freq, 'glc', [10, 11, 12])  # adding a new key
print('contents of the dictionary: ')
print(w_freq)

# search for particular value
value = 10
# get the list that contains the given value
list_of_keys = [key for key, list_of_values in w_freq.items() if value in list_of_values]
if list_of_keys:
    print(list_of_keys)
else:
    print("value does not exist in the dictionary")
