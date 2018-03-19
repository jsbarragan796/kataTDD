__author__ = 'Juan Sebastian Barragan'
import numpy as np

# Pedir al usuario los numeros en la consola
#stringNumbers = raw_input('Type your numbers separated by commas')

class Estadistic:

    def minMaxElement(self,string):
        if string == " " or string == "":
            return [0, None, None]
        elif "," in string:
            numbers = np.array(string.split(",")).astype(np.int)
            if numbers[0] > numbers[1]:
                return [2,numbers[1],numbers[0]]
            else:
                return [2, numbers[0], numbers[1]]
#            return [len(numbers),min(numbers)]
        else:
            return [1,int(string),int(string)]
