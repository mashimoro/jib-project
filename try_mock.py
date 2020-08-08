import unittest
from unittest.mock import patch
import getRendom  

class TetsRandom(unittest.TestCase):
  @patch('getRendom.random.randint')
  def test_it_should_call_andint_eith_1_and_10(self, mock):
    getRendom.get_rendom_number_plus_one()
    mock.assert_called_once_with(1,10)

  @patch('getRendom.random.randint')
  def test_it_should_get_4_when_random_get_3(self, mock):
    # mock.return_value = 3   stap mock
    mock.return_value = 3  
    result = getRendom.get_rendom_number_plus_one()
    self.assertEqual(result,4)
   
  def test_it_should_get_3(self):
    while True:
      result = getRendom.get_rendom_number_plus_one()
      if result == 3:
        break
    self.assertEqual(result ,3) 

# print(get_rendom_number_plus_one())
unittest.main()