def max_int_in_list(_list):
    maxi = _list[0]
    
    for index, value in enumerate(_list):
        if(value > maxi):
            maxi = value
        
    return maxi
    
my_list = [5, 2, -5, 10, 23, -21, 22]
biggest_int = max_int_in_list(my_list)
print biggest_int