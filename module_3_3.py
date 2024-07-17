def print_params(a =1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b=25, c=[1,2,3])

values_list = [1, 'q', False]
values_dict = {'a': 1, 'b': 'qq', 'c': 1.3}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, "'Строка'"]
print_params(*values_list_2, 42)