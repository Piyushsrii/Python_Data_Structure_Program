'''Write a Python program to get the current username'''
import getpass
class CurrentUser:
    def checkUser(self):
        '''
               :param :self
               :return:
              '''
        print(getpass.getuser())
userObj = CurrentUser()
userObj.checkUser()
