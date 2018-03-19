__author__ = 'Juan Sebastian Barragan'

# Pedir al usuario los numeros en la consola
#stringNumbers = raw_input('Type your numbers separated by commas')

class Estadistic:
    def elements(self, string):
        if string == " " or string == "":
            return [0]
        elif "," in string:
            numbers = string.split(",")
            return [len(numbers)]
        else:
            return [1]
