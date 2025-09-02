import unittest 

from unittest.mock import patch
from io import StringIO

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from main import skills_practice_math_ciel #import correct function



class TestSkillsPracticeMathCiel(unittest.TestCase): #change class name
    
    
    def setUp(self):

        self.original_stdout = patch('sys.stdout', new_callable=StringIO).start() 
        self.addCleanup(patch.stopall)
        

    def tearDown(self):
        pass

  
    
    def tests_skills_practice_math_ciel(self): #change name
    
        skills_practice_math_ciel() #changed function call
        output = self.original_stdout.getvalue().strip() 
        expected_output = "math.ceil(4.1) = 5\nmath.ceil(4) = 4\nmath.ceil(17) = 17\nmath.ceil(17.1) = 18\nmath.ceil(17.5) = 18\nmath.ceil(17.8) = 18" # change this

        self.assertEqual(
            output,
            expected_output,
            msg=f"\n❌ Wrong output.\nExpected: \n'{expected_output}'\nReceived: \n'{output}'"
        )


if __name__ == '__main__': 

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestSkillsPracticeMathCiel) #change input paramenter
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)


    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)
