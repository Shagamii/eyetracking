from datetime import datetime

from output_to_csv import output_to_csv

storage = []

def storatge_gaze_data(
    time_stamp,
    left_gaze_point_x,
    left_gaze_point_y,
    right_gaze_point_x,
    right_gaze_point_y,
    _path = "",
):

    gaze_data = {
        'time_stamp': time_stamp,
        'left_gaze_point_x': left_gaze_point_x,
        'left_gaze_point_y': left_gaze_point_y,
        'right_gaze_point_x': right_gaze_point_x,
        'right_gaze_point_y': right_gaze_point_y
    }
    storage.append(gaze_data)

    if len(storage) >= 1000:
        exec_storage_to_csv(_path=_path)

def exec_storage_to_csv(_path = ""):
    print(len(storage))
    start_time = datetime.fromtimestamp(storage[0]["time_stamp"]).strftime('%Y%m%d-%H%M%S')
    end_time = datetime.fromtimestamp(storage[-1]["time_stamp"]).strftime('%Y%m%d-%H%M%S')
    output_to_csv(gaze_data_list=storage, _path = _path if _path != '' else start_time + "-" + end_time)
    storage.clear()
