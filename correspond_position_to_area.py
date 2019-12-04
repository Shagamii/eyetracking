import math
from os.path import join

from get_formated_area_data import get_formated_area_data
from get_formated_gaze_data import get_formated_gaze_data
from import_csv import import_csv

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



if __name__ == '__main__':
    gaze_data = import_csv(
        join("shagamii",
             "20191106-045128-20191106-045148"), get_formated_gaze_data)
    area_data = import_csv(
        join("layout", "shagamii"), get_formated_area_data
    )[0]
    d = correspond_position_to_area(
        gaze_data=gaze_data,
        area_data=area_data
    )
    print(d)
