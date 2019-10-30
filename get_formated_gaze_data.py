from output_to_csv import CSV_HEADER

def get_formated_gaze_data(gaze_data):
    time_stamp = gaze_data[0]
    left_gaze_point_x, left_gaze_point_y, right_gaze_point_x, right_gaze_point_y = list(map(lambda x: float(x), gaze_data[1:5]))
    gaze_point_x = (left_gaze_point_x + right_gaze_point_x)/2
    gaze_point_y = (left_gaze_point_y + right_gaze_point_y)/2
    return [time_stamp, gaze_point_x, gaze_point_y]