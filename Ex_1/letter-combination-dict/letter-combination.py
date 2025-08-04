import itertools
def get_letter_combinations(data_dict):
    sorted_keys = sorted(data_dict.keys())
    character_lists = [data_dict[k] for k in sorted_keys]
    combinations = itertools.product(*character_lists)
    string_combinations = [''.join(combo) for combo in combinations]
    return string_combinations
my_dict = {'1': ['a', 'b'], '2': ['c', 'd']}
all_combinations = get_letter_combinations(my_dict)
print("All letter combinations:")
for combo in all_combinations:
    print(combo)
