import unittest 
# unittest is module which provides a built in framework to test each functions. 

from unittest.mock import patch
# unittest.mock is a submodule inside unittest.
# It provides tools to mock objects during testing (useful when testing code that uses input(), print(), databases, APIs, etc.)
# patch() lets you replace functions or variables temporarily during a test.

from io import StringIO


import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
#print("__file__ =", __file__)        # path of this file (1411/Assignment-Manager/assignment-manager/Lab-02-VScode_and_Github/Lab-02-Solution/Lab-02-test/tests/test_01_print_hello.py)
#os.path.dirname(__file__).  removes last file or folder and returns the path (1411/Assignment-Manager/assignment-manager/Lab-02-VScode_and_Github/Lab-02-Solution/Lab-02-test/tests)
#os.path.join    joins the given two paths. ie (1411/Assignment-Manager/assignment-manager/Lab-02-VScode_and_Github/Lab-02-Solution/Lab-02-test/tests/../../src)
#os.path.abspath    eleminates ../.. and returns absoulte path  ie(1411/Assignment-Manager/assignment-manager/Lab-02-VScode_and_Github/Lab-02-Solution/src)
#sys.path.insert(0,path). asks python to first check this before checking any other packages or modules)


from main import skills_practice_numbers # gets skills_practice_numbers from .../Lab-02-VScode_and_Github/Lab-02-Solution/src





class TestSkillsPracticeNumbers(unittest.TestCase):
    
    # Notes on self input parameter: explicitly accesses instance variables and methods of the current object.
    # In C++, the 'this' pointer performs the same task implicitly.
    
    def setUp(self):

        # Redirect stdout before each test
        # self.original_stdout is new variable being decalred and is assigned a StringIO object.
        # This object is now capturing everything that would normally be printed to the console using print().
        self.original_stdout = patch('sys.stdout', new_callable=StringIO).start() # "This is my first test. It should print out a message here: Hello World!"
        
        # Whatever happens, make sure to stop all patches after this test.
        self.addCleanup(patch.stopall)
        

    def tearDown(self):
        # Will be handled by addCleanup, but can include any extra cleanup here
        pass

  
    
    def tests_skills_practice_numbers(self):
        # Call the function
        skills_practice_numbers()

        # Get printed output
        output = self.original_stdout.getvalue().strip() # "This is my first test. It should print out a message here: Hello World!"

        # Expected output
        expected_output = "19 + 5 = 24\n18 - 5 = 13\n5 - 18 = -13\n18 * 5 = 90\n18 / 5 = 3.6\n5 / 18 = 0.2777777777777778\n6 ** 4 = 1296\n79 % 17 = 11\n79 // 17 = 4\n17 + 4 * 5 = 37\n(17 + 4) * 5 = 105\na + b = 19"

        # Assert
        self.assertEqual( # if output is not equal to expected_output then it prints msg
            output,
            expected_output,
            msg=f"\n❌ Wrong output.\nExpected: \n'{expected_output}'\nReceived: \n'{output}'"
        )


if __name__ == '__main__': # run this if its being run directly ie the main or else dont run this

    loader = unittest.TestLoader()
    # unittest.TestLoader.
    # TestLoader is a class defined in the unittest module.
    # Its purpose: load test cases and test methods from test classes or modules.
    # Think of it like a factory object that knows how to find tests.
    # unittest.TestLoader().
    # This calls the constructor of the TestLoader class.
    # Returns a new instance of TestLoader.
    # Assignment to loader.

    suite = loader.loadTestsFromTestCase(TestSkillsPracticeNumbers)
    # loader is now a TestLoader object (an instance of the TestLoader class).
    # It has methods you can call, like:
    # loadTestsFromTestCase()
    # loadTestsFromModule()
    # discover()


    runner = unittest.TextTestRunner(stream=sys.stderr)  
    # TextTestRunner = object that runs test suites and prints results.
    # stream=sys.stderr → prints logs to stderr (so stdout stays clean).
    # runner now holds a TextTestRunner object.
    
    
    result = runner.run(suite)
    # Calls the runner to execute all tests in the suite.
    # Returns a TestResult object (result) containing:
    # number of tests run
    # failures
    # errors
    # success/failure status
    # result is what you query to see if all tests passed.

    
    if result.wasSuccessful():
        print("Test passed")   # Goes to stdout (for autograder)
    else:
        print("Test failed")
        sys.exit(1)            # Non-zero exit code signals failure
