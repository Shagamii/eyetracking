from math import floor
# key,x,y,width,height
# page,0,0,1920,1080
# header,0,0,1920,30
# editor,450,30,1470,746
# editorRow,,,,26
# executor,0,776,1920,24
# terminal,0,800,1920,280
# question,0,30,450,746

def get_formated_area_data():
    # 今のところ共通なので決め打ちで

    page = [0,0,1920,1080]
    header = [0,0,1920,30]
    editor = [450,30,1470,746]
    editorRow = [None, None, None,26]
    executor = [0,776,1920,24]
    terminal = [0,800,1920,280]
    question = [0,30,450,746]

    def get_x(d):
        return d[0]
    def get_y(d):
        return d[1]
    def get_width(d):
        return d[2]
    def get_height(d):
        return d[3]

    def height_px_to_rate(px):
        return px/get_height(page)
    
    def width_px_to_rate(px):
        return px/get_width(page)
    
    header_area = ["header", 0, 1, 0, height_px_to_rate(get_height(header))]
    question_area = ["question", 0, width_px_to_rate(get_width(question)), height_px_to_rate(
            get_y(question)), height_px_to_rate(get_y(question) + get_height(question))]
    executor_area = ["executor", 0, 1, height_px_to_rate(get_y(executor)), height_px_to_rate(get_y(executor) + get_height(executor))]
    terminal_area = ["console", 0, 1, height_px_to_rate(get_y(terminal)), height_px_to_rate(get_y(terminal) + get_height(terminal))]
    formated_area_data = [
        header_area,
        question_area,
        executor_area,
        terminal_area,
    ]

    end_of_question_area_x = question_area[3]

    number_of_row = floor(get_height(editor)/get_height(editorRow))
    for i in range(number_of_row):
        formated_area_data.append([
            "textarea_row_" + str(i + 1),
            end_of_question_area_x,
            1,
            height_px_to_rate(i * get_height(editorRow) + get_y(editor)),
            height_px_to_rate((i + 1) * get_height(editorRow) + get_y(editor))
    ])
    formated_area_data.append([
        "textarea_row_" + str(number_of_row + 1), 
            end_of_question_area_x,
            1,
        height_px_to_rate(
            number_of_row * get_height(editorRow) + get_y(header)
        ),
        height_px_to_rate(get_y(executor)),
    ])
    # formated_area_data.append([
    #     "executor", 0, 1, px_to_rate( header + editor), px_to_rate( header + editor + executor)
    # ])
    # formated_area_data.append([
    #     "terminal", 0, 1, px_to_rate( header + editor + executor),  1
    # ])
    return formated_area_data
