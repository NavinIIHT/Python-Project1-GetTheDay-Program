

# import colorama
# from colorama import Fore
# colorama.init(autoreset=True)
import unittest
import sys
sys.path.append("..")
from count_chars import count_characters
from dateandday import get_week_day
class ExceptionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("output_exception_revised.txt","w") as f:
            pass
    def test_type_error_for_count(self):
        try:
            count_characters(15)
            with open("output_exception_revised.txt","a") as f:
                f.write("TestTypeErrorForCount=False\n")
                # print("{}TestTypeErrorForCount = {}Failed".format(Fore.YELLOW,Fore.RED))
                print("TestTypeErrorForCount = Failed")
        except TypeError:
            with open("output_exception_revised.txt","a") as f:
                f.write("TestTypeErrorForCount=True\n")
                # print("{}TestTypeErrorForCount = {}Passed".format(Fore.YELLOW,Fore.GREEN))
                print("TestTypeErrorForCount = Passed")

    def test_type_error_for_day(self):
        try:
            get_week_day(12-5-2021)
            with open("output_exception_revised.txt","a") as f:
                f.write("TestTypeErrorForDay=False\n")
                # print("{}TestTypeErrorForDay = {}Failed".format(Fore.YELLOW,Fore.RED))
                print("TestTypeErrorForDay = Failed")

        except TypeError:
            with open("output_exception_revised.txt","a") as f:
                f.write("TestTypeErrorForDay=True\n")
                # print("{}TestTypeErrorForDay = {}Passed".format(Fore.YELLOW,Fore.GREEN))
                print("TestTypeErrorForDay = Passed")
