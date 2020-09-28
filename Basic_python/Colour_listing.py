'''Write a Python program to print out a set containing all the colors from color_list_1 which
are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])ls
Expected Output White , Black'''
class ColorSet:
    def colorDiff(self,colourList1,colourList2):
        print(colorList1.difference(colorList2))
    '''
    :param self:
    :param colourList1:
    :param colourList2:
    :return:
    '''
colorList1 = set(["White", "Black", "Red"])
colorList2 = set(["Red", "Green"])
colorObj = ColorSet()
colorObj.colorDiff(colorList1,colorList2)


