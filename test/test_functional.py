
import unittest
import sys
sys.path.append("..")
from count_chars import count_characters
from dateandday import get_week_day
class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("../output_revised.txt","w") as f:
            pass
    def test_is_array(self):
        obj=count_characters("Karthik Age Is 18 @2021")
        if type(obj)==type([]):
            with open("../output_revised.txt","a") as f:
                f.write("TestIsArray=True\n")
                print("TestIsArray = Passed")

        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestIsArray=False\n")
                print("TestIsArray = Failed")

    def test_is_str(self):
        obj=get_week_day("12-5-2021")
        if type(obj)==type(" "):
            with open("../output_revised.txt","a") as f:
                f.write("TestIsString=True\n")
                print("TestIsString = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestIsString=False\n")
                print("TestIsString = Failed")
