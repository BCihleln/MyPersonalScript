
from sqlite3 import Time

from time import sleep


def DisplayLoading(Time):
    for i in range(0,Time):
        print(".",end="",flush="True")
        sleep(1)
    print("\n")