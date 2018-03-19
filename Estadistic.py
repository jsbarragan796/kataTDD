__author__ = 'Juan Sebastian Barragan'
import numpy as np

# Pedir al usuario los numeros en la consola
#stringNumbers = raw_input('Type your numbers separated by commas')

class Estadistic:

    def minElement(self,string):
        if string == " " or string == "":
            return [0, None]
        elif "," in string:
            numbers = np.array(string.split(",")).astype(np.int)
            return [len(numbers),min(numbers)]
        else:
            return [1,int(string)]
