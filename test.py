import unittest
import app
from numberToWord import convertNumToWord

class TestCase(unittest.TestCase):

    def testNumToWordFunction(self):
        self.assertEqual(convertNumToWord(""),"Please Enter Amount")
        self.assertEqual(convertNumToWord("23.3435ygh"),"Not a Valid Amount!")
        self.assertEqual(convertNumToWord("23435545245"),"Only Amount Between 00 to 999999.99 Supported!")
        self.assertEqual(convertNumToWord("0"),"Rs. Zero ONLY")
        self.assertEqual(convertNumToWord('122000.23'),"Rs. One Lakh Twenty Two Thousand 23/100 ONLY")
        self.assertEqual(convertNumToWord("10020.23"),"Rs. Ten Thousand Twenty 23/100 ONLY")
        self.assertEqual(convertNumToWord('456'),"Rs. Four Hundred Fifty Six ONLY")
        self.assertEqual(convertNumToWord('12.00'),"Rs. Twelve ONLY")
        self.assertEqual(convertNumToWord('5'),"Rs. Five ONLY")
        self.assertEqual(convertNumToWord('0.543'),"Rs. 54/100 ONLY")
        self.assertEqual(convertNumToWord(0.543),"Rs. 54/100 ONLY")

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
          

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")

    

    
