from datetime import datetime
from os.path import join

from output_to_csv import output_to_csv

storage = []

def storatge_gaze_data(
    time_stamp,
    left_gaze_point_x,
    left_gaze_point_y,
    right_gaze_point_x,
    right_gaze_point_y,
    dirname
):

    gaze_data = {
        'time_stamp': time_stamp,
        'left_gaze_point_x': left_gaze_point_x,
        'left_gaze_point_y': left_gaze_point_y,
        'right_gaze_point_x': right_gaze_point_x,
        'right_gaze_point_y': right_gaze_point_y
    }
    storage.append(gaze_data)

    if len(storage) >= 10000:
        exec_storage_to_csv(dirname=dirname)

def exec_storage_to_csv(dirname):
    print(len(storage))
    start_time = datetime.fromtimestamp(storage[0]["time_stamp"]).strftime('%Y%m%d-%H%M%S')
    end_time = datetime.fromtimestamp(storage[-1]["time_stamp"]).strftime('%Y%m%d-%H%M%S')
    _path = start_time + "-" + end_time
    output_to_csv(gaze_data_list=storage, _dirname = dirname, _path = _path)
    storage.clear()
