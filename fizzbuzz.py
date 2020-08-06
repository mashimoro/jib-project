#input หาร 3 ลงตัว return Fizz
#input หาร 5  ลงตัว return Buzz
#input หาร 3 , 5 ลงตัว  return FIZZ BUZZ
#input  ไม่เลย return input
#  run python ตรง ๆๆ __name__ = __main__ 
#  import file --> __name__ = __filename__

# def fizz(number):
#       if number == 3:
#           return 'Fizz'
# print(fizz(3))

import unittest
def fizzbuzz(number):
    if number == 1:
        return 1
    elif number % 3 == 0 :
        return 'Fizz'

class TestFizzBuzz(unittest.TestCase):
    def test_input_1_should_get_1(self):
        result = fizzbuzz(1)
        self.assertEqual(result,1)

    def test_input_3_return_Fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result,'Fizz')

unittest.main()