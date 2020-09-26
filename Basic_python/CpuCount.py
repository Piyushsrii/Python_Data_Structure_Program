'''Write a Python program to find out the number of CPUs using.'''
import multiprocessing
class CurrentProcess:
    def process(self):
        '''
        :param
        :param
        :return:
       '''
        print(multiprocessing.cpu_count())
current = CurrentProcess()
current.process()
