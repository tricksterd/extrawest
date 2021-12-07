from linked_list import *
import time
import sys

new_list = LinkedList()

for i in range(10):
    new_list.append(i)

old_list = [i for i in range(10)]


def mid_insertion():
    first_time = time.time()
    new_list.insert(new_list.len() // 2, 2)
    delta_1 = time.time() - first_time

    second_time = time.time()
    old_list.insert(len(old_list) // 2, 2)
    delta_2 = time.time() - second_time

    print(new_list, old_list)
    print(len(old_list), new_list.len())
    print('Mid insertion: \n Built-in list faster than my list on {}'.format(delta_1 - delta_2))


def begin_insertion():
    first_time = time.time()
    new_list.insert(0, 2)
    delta_1 = time.time() - first_time

    second_time = time.time()
    old_list.insert(0, 2)
    delta_2 = time.time() - second_time

    print(new_list, old_list)
    print(len(old_list), new_list.len())
    print('Start insertion: \nBuilt-in list faster than my list on {}'.format(delta_1 - delta_2))


def end_insertion():
    first_time = time.time()
    new_list.append(2)
    delta_1 = time.time() - first_time

    second_time = time.time()
    old_list.append(2)
    delta_2 = time.time() - second_time

    print(new_list, old_list)
    print(len(old_list), new_list.len())
    print('End insertion:\n Built-in list faster than my list on {}'.format(delta_1 - delta_2))


def mid_delete():
    first_time = time.time()
    new_list.pop(new_list.len() // 2)
    delta_1 = time.time() - first_time

    second_time = time.time()
    old_list.pop(len(old_list) // 2)
    delta_2 = time.time() - second_time

    print(len(old_list), new_list.len())
    print('Mid delete: \n Built-in list faster than my list on {}'.format(delta_1 - delta_2))


# begin_insertion()
# mid_insertion()
# end_insertion()
# mid_delete()

for i in range(1000000):
    new_list.append(i)
print(sys.getsizeof(new_list))