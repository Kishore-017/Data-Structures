import itertools
def get_all_combinations(input_list):
    all_combinations = []
    for r in range(len(input_list) + 1):
        combinations_of_length_r = list(itertools.combinations(input_list, r))  
        all_combinations.extend(combinations_of_length_r)  
    return all_combinations
my_list = ['A', 'B', 'C']
combinations = get_all_combinations(my_list)
print(f"Original list: {my_list}")
print("All possible combinations:")
for combo in combinations:
    print(combo)
