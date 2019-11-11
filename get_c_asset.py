from os.path import join, dirname

PROGRAM_FILE_NAMES = [
    "runtime_error",
    "compile_error",
    "result_error",
]

def get_c_asset(order_of_asset, asset_dirname, extension=".c"):
    if order_of_asset < 0 or len(PROGRAM_FILE_NAMES) < order_of_asset:
        return ""
    index_of_program = order_of_asset - 1
    program_file_name = PROGRAM_FILE_NAMES[index_of_program]
    c_file_path = join(dirname(__file__), "dist", "assets", "c", asset_dirname, program_file_name + extension)
    with open(c_file_path, encoding="utf-8") as f:
        return f.read()
