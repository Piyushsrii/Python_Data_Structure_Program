'''Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.'''
class SpecStringPart:
    def chkSpecCharacter(self,strVal):
        '''
        :param self:
        :param strVal:
        :return:
        '''
        l = strVal.split(",")
        t = tuple(l)
        print(l)
        print(t)
stringData = SpecStringPart()
strVal = input("Enter Words With , Separated Sequence : ")
stringData.chkSpecCharacter(strVal)