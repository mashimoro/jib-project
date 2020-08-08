import random
import unittest

class TetsRandom(unittest.TestCase):
  def test_it_should_get_3(self):
    while True:
      result = get_rendom_number_plus_one()
      if result == 3:
        break
    self.assertEqual(result ,3)
  
  

def get_rendom_number_plus_one():
  return random.randint(1 ,10) + 1

# print(get_rendom_number_plus_one())
unittest.main()