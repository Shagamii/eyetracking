from datetime import datetime

from get_correct_time_stamp import get_correct_time_stamp
from storage_gaze_data import storatge_gaze_data, exec_storage_to_csv

initial_device_time_stamp = None
initial_system_time_stamp = None
start_time = datetime.today()

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

    storatge_gaze_data(
        time_stamp=get_correct_time_stamp(
            time_stamp=system_time_stamp,
            start_time=start_time,
            initial_time_stamp=initial_system_time_stamp
        ),
        left_gaze_point_x=left_gaze_point_x,
        left_gaze_point_y=left_gaze_point_y,
        right_gaze_point_x=right_gaze_point_x,
        right_gaze_point_y=right_gaze_point_y
    )