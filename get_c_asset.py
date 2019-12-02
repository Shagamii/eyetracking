from os.path import join, dirname

PROGRAM_FILE_NAMES = [
    "assignment",
    "pointer",
    "pointer2",
    "pointer4",
    "recursive",
    "type_of_variable",
    "compile_error",
    "runtime_error",
    "result_error",
    "control"
]

def get_program_file_name_from_order (order_of_asset):
    index_of_program = order_of_asset - 1
    if len(PROGRAM_FILE_NAMES) < order_of_asset:
         return None
    return PROGRAM_FILE_NAMES[index_of_program]

def get_c_asset(order_of_asset, asset_dirname, extension=".c"):
    if order_of_asset < 0 or len(PROGRAM_FILE_NAMES) < order_of_asset:
        return ""
    program_file_name = get_program_file_name_from_order(order_of_asset=order_of_asset)
    if program_file_name == None:
        return ''
    c_file_path = join(dirname(__file__), "dist", "assets", "c", asset_dirname, program_file_name + extension)
    with open(c_file_path, encoding="utf-8") as f:
        return f.read()
