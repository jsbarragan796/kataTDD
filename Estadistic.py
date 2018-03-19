__author__ = 'Juan Sebastian Barragan'

# Pedir al usuario los numeros en la consola
#stringNumbers = raw_input('Type your numbers separated by commas')

class Estadistic:
    def elements(self, string):
        if string==" ":
            return 0
        elif string=="1":
            return 1
        else:
            return 2