from os.path import join, dirname

PROGRAM_FILE_NAMES = [
    "compile_error",
    "result_error",
    "runtime_error"
]

def get_c_program(order_of_program):
    if order_of_program < 0 or len(PROGRAM_FILE_NAMES) < order_of_program:
        return ""
    index_of_program = order_of_program - 1
    program_file_name = PROGRAM_FILE_NAMES[index_of_program]
    c_file_path = join(dirname(__file__), "dist", "assets", "c", program_file_name + ".c")
    with open(c_file_path, encoding="utf-8") as f:
        return f.read()