import unittest
from MainFile import SolveForX, check_type, Sequence


class TestCheckType(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPassingValue(self):
        """
        Tests for the passing of integers
        """
        error_message = "That should be an integer or a floating point number."
        typechecker = check_type(4, (int, float), error_message)
        self.assertTrue(typechecker)

    def testFailingValue(self):
        """
        Tests for the failure of a string given an int type
        """
        error_message = "That should be an integer or a floating point number."
        with self.assertRaises(TypeError):
            check_type("Hey there", (int, float), error_message)


class TestSolveForX(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMultiply_integer(self):
        """
        Tests for ints
        """

        test_instance = SolveForX(y=3, z=9)
        test_x = test_instance.multiply()
        self.assertEqual(test_instance.z, test_instance.y*test_x)

    def testMultiply_float(self):
        """
        Tests for floats
        """

        test_instance = SolveForX(y=3.4, z=9.8)
        test_x = test_instance.multiply()
        self.assertEqual(test_instance.z, test_instance.y*test_x)

    def testDivide_integer(self):
        """
        Tests for ints
        :return: Pass
        """

        test_instance = SolveForX(y=4, z=3)
        test_x = test_instance.divide()
        self.assertEqual(test_instance.z, test_x/test_instance.y)

    def testDivide_float(self):
        """
        Tests for floats
        :return: Pass
        """

        test_instance = SolveForX(y=4.6, z=3.2)
        test_x = test_instance.divide()
        self.assertEqual(test_instance.z, test_x/test_instance.y)

    def testExponent_integer(self):
        """
        Tests for ints
        :return: Pass
        """

        test_instance = SolveForX(y=3, z=81)
        test_x = test_instance.exponent()
        self.assertEqual(test_instance.z, test_instance.y**test_x)

    def testExponent_float(self):
        """
        Tests for floats
        :return: Pass
        """

        test_instance = SolveForX(y=3, z=81)
        test_x = test_instance.exponent()
        self.assertEqual(test_instance.z, test_instance.y**test_x)


class TestSequences(unittest.TestCase):

    def setUp(self):
        self.testlimit = 10
        self.testSequence = Sequence(self.testlimit)
        self.testSequence.fibonacci()

    def tearDown(self):
        pass

    def testAssignment(self):
        """
        Test that the value we assigned is where it is supposed to be
        """
        self.assertEqual(self.testSequence.limit, self.testlimit)

    def testFinalAnswer(self):
        """
        Test to ensure that the final fibonacci number is indeed the one we are looking for
        """
        self.assertEqual(self.testSequence.fibonacci(), 34)

    def testAssignmentViaMethod(self):
        """
        Test to make sure that fibonacci() method assigns limit_value to self
        """
        self.assertEqual(self.testSequence.fibonacci(), self.testSequence.limit_value)

    def testFibonacciList(self):
        """
        Test that the last
        """
        self.assertTrue(len(self.testSequence.fibonacci_sequence) == self.testlimit)

if __name__ == "__main__":
    unittest.main()
