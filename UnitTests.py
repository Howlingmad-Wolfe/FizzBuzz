#bin/python
import unittest
import random

from FizzBuzz import FizzBuzz

class FizzBuzzUnitTest (unittest.TestCase):
          
    def test_InputDefault(self):
        testInputDefault = FizzBuzz()
        default = range(101)
        self.assertEquals(testInputDefault.input, default)
        
    def test_InputNonDefault(self):
        for i in range(10):
            testInputSet = range(int(random.randrange(3000)))
            testInputRandom = FizzBuzz(testInputSet)
            self.assertEquals(testInputRandom.input, testInputSet)
        
    def test_PlayFizzBuzzWithInputDefault(self):
        testInstance = FizzBuzz()
        testSet = range(101)
        fizzBuzzedSet = testInstance.PlayFizzBuzz()
        for i in testSet:            
            if i % 3 == 0 and i % 5 != 0:
                self.assertEquals(fizzBuzzedSet[i], "Fizz", "PlayFizzBuzz() returned " + str(fizzBuzzedSet[i]) + " Not 'Fizz'!")
            elif i % 5 == 0 and i % 3 != 0:
                self.assertEquals(fizzBuzzedSet[i], "Buzz", "PlayFizzBuzz() returned " + str(fizzBuzzedSet[i]) + " Not 'Buzz'!")
            elif i % 3 == 0 and i % 5 == 0:
                self.assertEquals(fizzBuzzedSet[i], "FizzBuzz", "PlayFizzBuzz() returned " + str(fizzBuzzedSet[i]) + " Not 'FizzBuzz'!")
            else:
                self.assertEquals(fizzBuzzedSet[i], i, "PlayFizzBuzz() returned " + str(fizzBuzzedSet[i]) + " Not " + str(i))
    
    def test_PlayFizzBuzzWithInputRandom(self):
        testSet = range((random.randrange(3001)))
        testInstance = FizzBuzz(testSet)
        fizzBuzzedSet = testInstance.PlayFizzBuzz()
        for i in testSet:  
            if i % 3 == 0 and i % 5 != 0:
                self.assertEquals(fizzBuzzedSet[i], "Fizz", "PlayFizzBuzz() returned " + str(fizzBuzzedSet[i]) + " Not 'Fizz'!")
            elif i % 5 == 0 and i % 3 != 0:
                self.assertEquals(fizzBuzzedSet[i], "Buzz", "PlayFizzBuzz() returned " + str(fizzBuzzedSet[i]) + " Not 'Buzz'!")
            elif i % 3 == 0 and i % 5 == 0:
                self.assertEquals(fizzBuzzedSet[i], "FizzBuzz", "PlayFizzBuzz() returned " + str(fizzBuzzedSet[i]) + " Not 'FizzBuzz'!")
            else:
                self.assertEquals(fizzBuzzedSet[i], i, "PlayFizzBuzz() returned " + str(fizzBuzzedSet[i]) + " Not " + str(i))
                
            

if __name__ == "__main__":
    unittest.main() 