def convert(array):
    c_list = array
    f_list = []
    for c in c_list:
        f = c*9./5+32
        f_list.append(f)
    return f_list
