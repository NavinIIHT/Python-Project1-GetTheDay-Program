import unittest
import sys
sys.path.append("..")
from dateandday import get_month_days

class BoundaryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("../output_boundary_revised.txt","w") as f:
            pass
    def test_month_not_in_range(self):
        x=get_month_days(15,2021)
        if x==-1:
            with open("../output_boundary_revised.txt","a") as f:
                f.write("TestMonthNotInRange=True\n")
                print("TestMonthNotInRange = Passed")
        else:
            with open("../output_boundary_revised.txt","a") as f:
                f.write("TestMonthNotInRange=False\n")
                print("TestMonthNotInRange = Failed")

    def test_month_in_range(self):
        x=get_month_days(4,2021)
        if x!=-1:
            with open("../output_boundary_revised.txt","a") as f:
                f.write("TestMonthInRange=True\n")
                print("TestMonthInRange = Passed")
        else:
            with open("../output_boundary_revised.txt","a") as f:
                f.write("TestMonthInRange=False\n")
                print("TestMonthInRange = Failed")
