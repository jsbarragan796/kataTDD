__author__ = 'Juan Sebastian Barragan'
import numpy as np

# Pedir al usuario los numeros en la consola
#stringNumbers = raw_input('Type your numbers separated by commas')

class Estadistic:

    def minMaxPromElement(self,string):
        if string == " " or string == "":
            return [0, None, None, None]
        elif "," in string:
            numbers = np.array(string.split(",")).astype(np.int)
            return [len(numbers), min(numbers), max(numbers)]
        else:
            return [1, int(string), int(string)]
