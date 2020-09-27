'''Write a Python program to get an absolute file path.'''
import os
class AbsolutePath:
    def absFilePath(self,filename):
        '''
                   :param:self
                   :param:filename
                   :return:
                   '''
        return os.path.abspath(filename)

pathObj = AbsolutePath()
fileName = input("Enter The Name Of The File With Extension : ")
print("Absolute file path: ", pathObj.absFilePath(fileName))