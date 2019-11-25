import time
import json
import datetime
from os.path import join

import tobii_research as tr

from apply_licenses import apply_licenses
from storage_gaze_data import exec_storage_to_csv
from gaze_data_callback import create_gaze_data_callback, get_extra_dirname_saved_csv

def subscribe_eyetracking(dirname):

    found_eyetrackers = tr.find_all_eyetrackers()
    my_eyetracker = found_eyetrackers[0]
    apply_licenses(my_eyetracker)
    print("Address: " + my_eyetracker.address)
    print("Model: " + my_eyetracker.model)
    print("Name (It's OK if this is empty): " + my_eyetracker.device_name)
    print("Serial number: " + my_eyetracker.serial_number)

    gaze_data_callback = create_gaze_data_callback(dirname)
    my_eyetracker.subscribe_to(
        tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

    def unsubscribe_eyetracking():
        extra_dirname_saved_csv = get_extra_dirname_saved_csv()[0]
        _dirname = join(dirname , extra_dirname_saved_csv) if extra_dirname_saved_csv != None else dirname
        my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
        exec_storage_to_csv(_dirname)
    
    return unsubscribe_eyetracking
