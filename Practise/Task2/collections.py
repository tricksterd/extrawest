def list_from_string(name, letter, patron):
    temp_list = list(name.strip().lower().replace('r', letter).replace('ddd', patron).title())
    temp_list.sort()
    return temp_list


def replace_letter(temp_list):
    for i in range(len(temp_list)):
        if temp_list[i] == 'а':
            temp_list[i] = 'А'
    return temp_list


full_name = " козявко Rеонід DdD"
my_list = list_from_string(full_name, 'Л', 'Олександрович')
my_list = replace_letter(my_list)
my_uniq_list = list(set(my_list))
print(len(my_uniq_list))
dict_0 = {item: ord(item) for item in my_uniq_list}
print(dict_0['А'])
# print(D['a']) It's error


new_name = ' папуша Rергей DdD'
new_list = list_from_string(new_name, 'C', 'Отчество')
new_list = replace_letter(new_list)
new_uniq_list = list(set(new_list))
print(len(new_uniq_list))
dict_1 = {item: ord(item) for item in new_uniq_list}
print(dict_1['А'])
# print(D['a']) It's error


dict_0.update(dict_1)

first_set = set(dict_0.keys())
second_set = set(dict_1.keys())

first_set.update(second_set)

final_list = [keys for keys in dict_0]

for i in first_set:
    if i in final_list:
        continue
    else:
        print("Final_list don't have this symbol {}".format(i))
