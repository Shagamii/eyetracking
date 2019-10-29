import sys
import time

from eyetracking import subscribe_eyetracking
from utils.get_index import get_index

def get_second_of_sleep():
    index_of_second = get_index(sys.argv, '--second')
    return index_of_second if index_of_second != False else 10

if __name__ == '__main__':
    unsubscribe_eyetracking = subscribe_eyetracking()
    second_of_sleep = get_second_of_sleep()
    time.sleep(second_of_sleep)
    unsubscribe_eyetracking()
