import unittest
import numpy as np
import sys
sys.path.insert(0, 'src/')

from Lamel_window.proccesing import Speed_of_Buble as moduls
from Lamel_window.proccesing import Filter_for_data

class TestFluidCube(unittest.TestCase):
    def testFluid(self):

        model = moduls.read_for_arr(np.array([]))
        self.AssertModelStep(model)

        model = moduls.read_for_arr(np.array([1, 1, 1, 1]))
        self.AssertModelStep(model)

        return True

    def CriationAssert(self, model):
        try:
            local_m = Filter_for_data()
        except:
            print("An error occurred during the step function!")
            return False
        local_m = Filter_for_data()
        model = moduls.read_for_arr(np.array([1, 1, 1, 1]))
        self.AssertModelStep(model)
        return True

def run_tests():
    unittest.main()


if __name__ == '__main__':
    run_tests()
