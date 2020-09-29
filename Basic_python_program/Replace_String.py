'''User Input and Replace String Template “Hello <<UserName>>, How are you?”'''
import string
from pythonProject1.venv.ReplaceString import str3, str1, str2
class ReplaceValue:
    def replaceString(self):
        str1 = "Hello, \n"
        str2 = "How are you"
        str3 = "UserName"
    print("The Statement is ")
    print("'", str1, str3, str2, "'")
rep = input("\nEnter the Replacing String for 'UserName': ")
if len(rep) >= 3:
    print("\nString can be Replaced")
    print("\nStatement Before Replacing")
    print(str1, str3, str2)
    print("\nStatement After Replacing")
    repl = str.replace(str3, str3, rep)
    print("'", str1, repl, str2, "'")
else:
    print("!!! String cannot be Replaced !!!")
    if __name__=='__main__':
       caller=ReplaceValue()
       caller.replaceString()
