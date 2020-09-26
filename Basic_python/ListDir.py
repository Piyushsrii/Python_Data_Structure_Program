'''Write a Python program to list all files in a directory in Python.'''
from os import listdir
from os.path import isfile
class ListFiles:
    def file(self):
        '''
                   :param
                   :param
                   :return:
                   '''
        filesList = [ ]
        for f in listdir('./'):
            if isfile(f):
                filesList.append(f)
        print(filesList)

fileObj = ListFiles()
fileObj.file()