import unittest
import numpy as np
import sys
sys.path.insert(0, 'src/')

from Lamel_window.proccesing import Speed_of_Buble as moduls


class TestFluidCube(unittest.TestCase):
    def testFluid(self):

        model = moduls.read_for_arr(np.array([]))
        self.AssertModelStep(model)

        return True


def run_tests():
    unittest.main()


if __name__ == '__main__':
    run_tests()
