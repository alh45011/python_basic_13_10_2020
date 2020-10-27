from collections import defaultdict

def get_elements_without_repetitions(arg_list):
    defaultdict_example = defaultdict(int)

    for idx in range(0, len(arg_list)):
        defaultdict_example[arg_list[idx]] = defaultdict_example[arg_list[idx]] + 1

    for key,value in defaultdict_example.items():
        if value == 1:
            yield key


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_iter = list(get_elements_without_repetitions(my_list))
print(my_iter)
