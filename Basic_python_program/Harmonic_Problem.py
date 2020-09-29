'''Harmonic Number'''
from pythonProject.Basic_python.Execution_Time import n
class Harmonic:
    def harmoni(self):
        '''
                      :param:self
                      :return
                     '''
        n= int(input("enter the value of n"))
        s=0.0
for i in range(1, n + 1):
        s = s + 1 / i ;
        print("Sum is", round(s,3))
        if __name__=='__main__':
                calling=Harmonic()
                calling.harmoni()