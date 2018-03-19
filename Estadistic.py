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
    def minElement(self,string):
        resp = self.elements(string)
        if string == " " or string == "":
            return [resp[0], None]
        elif "," in string:
            numbers = string.split(",")
            if(int(numbers[0])>int(numbers[1])):
                return [resp[0],int(numbers[1])]
            else:
             return [resp[0],int(numbers[0])]
        else:
            return [resp[0],int(string)]
