
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

    def test_to_count_characters(self):
        obj=count_characters("Karthik Age Is 18 @2021")
        if obj!=None:
            if obj[0]==9 and obj[1]==3 and obj[2]==6 and obj[3]==1:
                with open("../output_revised.txt","a") as f:
                    f.write("TestToCountCharacters=True\n")
                    print("TestToCountCharacters = Passed")
            else:
                with open("../output_revised.txt","a") as f:
                    f.write("TestToCountCharacters=False\n")
                    print("TestToCountCharacters = Failed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestToCountCharacters=False\n")
                print("TestToCountCharacters = Failed")

    def test_is_day(self):
        day=get_week_day("12-9-2021")
        if day=="Sunday":
            with open("../output_revised.txt","a") as f:
                f.write("TestIsDay=True\n")
                print("TestIsDay = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestIsDay=False\n")
                print("TestIsDay = Failed")
