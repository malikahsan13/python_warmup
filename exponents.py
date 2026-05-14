# print (2**3)


def calc_cube(base_num, pow_num):
    result = 1
    for num in range(pow_num):
        result = result * base_num
    return result
    
print(calc_cube(2, 3))