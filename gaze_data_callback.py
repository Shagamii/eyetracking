from datetime import datetime
from os.path import join

from get_correct_time_stamp import get_correct_time_stamp
from storage_gaze_data import storatge_gaze_data, exec_storage_to_csv

initial_device_time_stamp = None
initial_system_time_stamp = None
start_time = datetime.today()

extra_dirname_saved_csv = None
before_extra_dirname_saved_csv = None

def get_extra_dirname_saved_csv():
    global extra_dirname_saved_csv, before_extra_dirname_saved_csv
    return [extra_dirname_saved_csv, before_extra_dirname_saved_csv]

def set_extra_dirname_saved_csv(dirname):
    global extra_dirname_saved_csv, before_extra_dirname_saved_csv
    before_extra_dirname_saved_csv = extra_dirname_saved_csv
    extra_dirname_saved_csv = dirname

def create_gaze_data_callback(dirname):
    def gaze_data_callback(gaze_data):
        device_time_stamp = gaze_data['device_time_stamp']
        system_time_stamp = gaze_data["system_time_stamp"]

        left_gaze_point=gaze_data['left_gaze_point_on_display_area']
        left_gaze_point_x, left_gaze_point_y = left_gaze_point

        right_gaze_point=gaze_data['right_gaze_point_on_display_area']
        right_gaze_point_x, right_gaze_point_y = right_gaze_point

        global initial_device_time_stamp, initial_system_time_stamp
        if initial_device_time_stamp == None:
            initial_device_time_stamp = device_time_stamp
            initial_system_time_stamp = system_time_stamp

        extra_dirname_saved_csv, before_extra_dirname_saved_csv= get_extra_dirname_saved_csv()

        if before_extra_dirname_saved_csv != None and extra_dirname_saved_csv != before_extra_dirname_saved_csv:
            set_extra_dirname_saved_csv(extra_dirname_saved_csv)
            _dirname = join(dirname , before_extra_dirname_saved_csv) if before_extra_dirname_saved_csv != None else dirname
            exec_storage_to_csv(_dirname)
            return

        _dirname = join(dirname , extra_dirname_saved_csv) if extra_dirname_saved_csv != None else dirname
        storatge_gaze_data(
            time_stamp=get_correct_time_stamp(
                time_stamp=system_time_stamp,
                start_time=start_time,
                initial_time_stamp=initial_system_time_stamp
            ),
            left_gaze_point_x=left_gaze_point_x,
            left_gaze_point_y=left_gaze_point_y,
            right_gaze_point_x=right_gaze_point_x,
            right_gaze_point_y=right_gaze_point_y,
            dirname=_dirname
        )
    return gaze_data_callback
