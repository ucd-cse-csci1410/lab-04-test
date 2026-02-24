import unittest 

from unittest.mock import patch
from io import StringIO

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.main import trim_cost #import correct function



class TestTrimCost(unittest.TestCase): #change class name
    
    
    def setUp(self):

        self.original_stdout = patch('sys.stdout', new_callable=StringIO).start() 
        self.addCleanup(patch.stopall)
        

    def tearDown(self):
        pass

    @patch('builtins.input', side_effect =['10', '5'])  # Mock user input
    def tests_trim_cost(self,mock_input): #change name
    
        trim_cost() #changed function call
        output = self.original_stdout.getvalue().strip() 
        expected_output = "Perimeter of the box = 30.0\nNumber of trims you need to buy = 3\nTotal cost of the trims = 5.64\nThe amount of trims lost = 0.5\nThe cost lost by wasting the trim = 0.94" # change this

        self.assertEqual(
            output,
            expected_output,
            msg=f"\n❌ Wrong output.\n Please Check the calculation and the format of the display'"
        )

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestTrimCost))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)
