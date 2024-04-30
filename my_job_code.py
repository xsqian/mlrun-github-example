import time
from src.greetings import greeting
from src.package1 import func1
from src.package1 import func2

def handler():
    for i in range(6):
        print("english")
        print(greeting())
        print(func1("hello f1"))
        print(func2("hello f2")) 
        time.sleep(1)
