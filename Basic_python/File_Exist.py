'''Write a Python program to check whether a file exists.'''
import os.path
from os import path

def main():
    '''
    :param:
    :return:
    '''
    print ("File exists:"+str(path.exists('main.py')))
    print ("File exists:" + str(path.exists('Calender.py')))

if __name__== "__main__":
   main()