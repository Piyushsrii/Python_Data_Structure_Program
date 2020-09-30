'''Write a program WindChill.java that takes two double command-line arguments t
and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
National Weather Service defines the effective temperature (the wind chill) to be:'''
class WindProgram :
    def WindChill(temp, velocity):
        """
        :param temp: temp input is taken
        :param velocity:  velocity input is taken
        :return:
        """
        power = math.pow(velocity, 0.6)
        total = 35.47 + 0.6215 * temp + (0.4275 * temp + 35.75) * power
        # total function is used for the calculation
        print(total)
        return total
# this program is created toc calculate wind chills by user input
if __name__ == '__main__':
        try:  # try is used for catching any error
            temp = int(input("enter temp below 50 in fahrenheit : "))
            if temp >= 51:
                print("enter between 50 and 1000")
            velocity = int(input("enter velocity in range of 3m/s and  120m/s : "))
            if velocity <= 4 or velocity >= 121:
                print("enter number between 3 and 120 ")
            calling=WindProgram()
            calling.WindChill(temp, velocity)
        except ValueError:  # if error is found then below statement will be printed
            print("check the input")