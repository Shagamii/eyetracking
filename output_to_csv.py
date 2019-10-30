import csv
from os.path import join, dirname

CSV_HEADER = [
    'time_stamp',
    'left_gaze_point_x',
    'left_gaze_point_y',
    'right_gaze_point_x',
    'right_gaze_point_y'
]

def output_to_csv(gaze_data_list, _path):
    csv_path = join(dirname(__file__), "..", "data" , _path + ".csv")
    with open(csv_path, 'w', newline="") as f:
        writer = csv.DictWriter(f, CSV_HEADER)
        writer.writerows(gaze_data_list)
