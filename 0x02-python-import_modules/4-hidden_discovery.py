#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dir_list = dir(hidden_4)
    for name in range(1, len(dir_list)):
        if "__" in dir_list[name]:
            continue
        print("{}".format(dir_list[name]))
