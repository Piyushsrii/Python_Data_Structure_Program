'''Desc -> Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks'''
from datetime import datetime
class StopWatchProgram() :
    def StopWatch(self):
        """
        :return: time in sec is returned if pressed enter
        """
    start = datetime.datetime.now()
    if input("plz enter to stop the program "):
        end = datetime.datetime.now()
        # prints time lapse
        print(abs(end - start))
if __name__ == '__main__':
        # when user will press enter then stopwatch will work
        caller = StopWatchProgram()
        caller.StopWatch()