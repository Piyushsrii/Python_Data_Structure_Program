'''Write a python program to call an external command in Python.'''

from subprocess import call
class ExternalCmd:
    def checkCmd(self,inputCmd):
        '''
           :param
           :param
           :return:
           '''
        listValue = inputCmd.split(" ")
        call(inputCmd)

inputCmd = input("Enter The Command  : ")
cmdObj = ExternalCmd()
cmdObj.checkCmd(inputCmd)