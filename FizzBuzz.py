#bin/python

class FizzBuzz ():
    input = []
    
    def __init__(self, input = None):
        if input == None:
            self.input = range(101)
        else:
            self.input = input
        
    def PlayFizzBuzz(self):
        output = []
        for i in self.input:
            if i % 3 == 0 and i % 5 == 0:
                output.append("FizzBuzz")
            elif i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")           
            else:
                output.append(i)
        return output        