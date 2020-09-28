'''rite a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False'''
def is_group_member(group_data, n):
    '''
    :param self:
    :param strVal:
    :return:
    '''
    for value in group_data:
        if n == value:
            return True
    return False
n1=int(input("Enter the value"))
n2=int(input("Enter the value"))
print(is_group_member([1, 5, 8, 3], n1))
print(is_group_member([5, 8, 3], n2))