import unittest
import tests_12_3 as tests

test = unittest.TestSuite()
test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests.RunnerTest))
test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests.TournamentTest))

launch_test = unittest.TextTestRunner(verbosity=2)
launch_test.run(test)
