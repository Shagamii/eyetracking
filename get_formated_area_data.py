from math import floor
    # "page",
    # "header",
    # "editor",
    # "editorRow",
    # "executor",
    # "terminal"

def get_formated_area_data(area_data):
    page, header, editor, editorRow, executor, terminal = list(map(lambda x: float(x), area_data))
    def px_to_rate(px):
        return px/page
    
    formated_area_data = [["header", 0, 1, 0, px_to_rate(header)]]
    number_of_row = floor(editor/editorRow)
    for i in range(number_of_row):
        formated_area_data.append([
            "editorRow" + "_" + str(i),
            0,
            1,
            px_to_rate(i * editorRow + header) if i != 0 else px_to_rate(header),
            px_to_rate((i+1) * editorRow + header)
            ])
    formated_area_data.append([
        "edge_of_editor", 0, 1, px_to_rate(number_of_row * editorRow + header), px_to_rate( header + editor)
    ])
    formated_area_data.append([
        "executor", 0, 1, px_to_rate( header + editor), px_to_rate( header + editor + executor)
    ])
    formated_area_data.append([
        "terminal", 0, 1, px_to_rate( header + editor + executor),  1
    ])
    return formated_area_data
