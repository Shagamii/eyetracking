import time
import json
import datetime

import tobii_research as tr

from apply_licenses import apply_licenses
from storage_gaze_data import exec_storage_to_csv
from gaze_data_callback import gaze_data_callback

def subscribe_eyetracking():
    found_eyetrackers = tr.find_all_eyetrackers()
    my_eyetracker = found_eyetrackers[0]
    apply_licenses(my_eyetracker)
    print("Address: " + my_eyetracker.address)
    print("Model: " + my_eyetracker.model)
    print("Name (It's OK if this is empty): " + my_eyetracker.device_name)
    print("Serial number: " + my_eyetracker.serial_number)

    my_eyetracker.subscribe_to(
        tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
    # time.sleep(30)

    def unsubscribe_eyetracking():
        my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
        exec_storage_to_csv()
    
    return unsubscribe_eyetracking
