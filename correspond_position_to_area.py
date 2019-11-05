from get_formated_gaze_data import get_formated_gaze_data
from import_csv import import_csv
import math

from utils.find_from_list import find_from_list

NONE_LABEL = "OUT_OF_EDITOR"
# type gaze_data = List[[time_stamp: str | float, x: float, y: float]]
# area_data = List[[label: string, min_x: float, max_x: float, min_y: float, max_y: float]]
# dimension = int
# return type = Dic[{ time_stamp, gaze_point_x, gaze_point_y, label }]
def correspond_position_to_area(gaze_data, area_data):
    def map_data_to_area(data):
        time_stamp, x, y = data

        if math.isnan(x) or math.isnan(y):
            return {
                'time_stamp': time_stamp,
                'gaze_point_x': x,
                'gaze_point_y': y,
                'label': NONE_LABEL
            }

        def inArea(_area):
            _, min_x, max_x, min_y, max_y = _area
            return min_x < x and x < max_x and min_y < y and y < max_y

        area = find_from_list(
            iterable=area_data,
            callback=inArea,
            default=None
        )

        if area == None:
            return {
                'time_stamp': time_stamp,
                'gaze_point_x': x,
                'gaze_point_y': y,
                'label': NONE_LABEL
            }

        label = area[0]
        return {
            'time_stamp': time_stamp,
            'gaze_point_x': x,
            'gaze_point_y': y,
            'label': label
        }

    return list(map(map_data_to_area, gaze_data))


# area_data = [
#     ['sidebar', 0, 0.18, 0, 1],
#     ['header', 0.18, 1, 0.083, ]
# ]

list(map(range()))
if __name__ == '__main__':
    gaze_data = import_csv(
        "20191029-125128-20191029-125139", get_formated_gaze_data)
    d = correspond_position_to_area(
        gaze_data,
        area_data=[
            [str(i*1000) + 0.04, (i % 2) * .5 + 0.04, ((i % 2) + 1) * .5, (i)/10, (i+1)/10] for i in range(10)
        ]
    )
    print(d)
