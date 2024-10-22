my_dict = {'Fedya': 1999, 'Inna': 2002, 'Alisa': 1997}
print('Dict:', my_dict)
print('Existing value:', my_dict['Alisa'])
my_dict['Roman'] = 2004
print('Missing dictionary value:', my_dict)
my_dict.update({'Irina': 1988,
           'Egor': 2001})
print('Two random pairs:', my_dict)
a = my_dict.pop('Fedya')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
my_set = {'Ivan', 'Kolya', 'Ivan', 'Makar', 'Ivan', 11, 12, 13, 14, 15, 15, 14, 13, 0.5, 0.5, 0.6, 0.6, 0.7, 0.7}
print("Set:", my_set)
my_set = {'Ivan', 'Ivan', 'Ivan', 11, 12, 13, 14, 15, 11, 12, 13, 14,
          (15, 14, 13)} # почему 1-ые два множества не уникальны?
print("Set:", my_set)
my_set = {5, 6, 7, 8, 9, 9, 8, 7, 6, 5}
print("Set:", my_set)
print(my_set.add(4)) # почему в методе "add" нельзя добавить сразу два элемента
print(my_set.add('Ivan'))
print(my_set)
print(my_set.discard('Ivan'))
print(my_set)
print("Modified set:", my_set)