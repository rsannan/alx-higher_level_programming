#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for item in range(list_length):
        try:
            result = my_list_1[item] / my_list_2[item]
            new_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
            result = 0
            new_list.append(result)
        except IndexError:
            print("out of range")
            return new_list
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
            new_list.append(result)
    return new_list
