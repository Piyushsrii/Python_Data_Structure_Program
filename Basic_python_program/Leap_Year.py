'''Flip Coin and print percentage of Heads and Tails'''
class LeapYear:
   def leapyear(self):
    year=int(input('enter year'))
    if year%100==0: #century year
       if year%400==0:
           print ('{} is leap year'.format(year))
       else:
          print ('{} is not leap year'.format(year))
    else:
       if year%4==0:
          print ('{} is leap year'.format(year))
       else:
         print ('{} is not leap year'.format(year))
    if __name__=='__main__':
        obj=LeapYear()
        obj.leapyear()

