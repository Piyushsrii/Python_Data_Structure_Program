'''Write a Python program to display formatted text (width=50) as output.'''
import textwrap
class FormattedText:

    #create this method for a formatted ouput
    def dispFormatText(self,strVal):
        '''
              :param:strVal: Set the length
              :return : Fixed 50 width
               '''
        print(textwrap.fill(strVal, width=50))
stringData = FormattedText()
strVal = input("Enter a Paragraph : ")
if __name__=="__main__":
    stringData.dispFormatText(strVal)
