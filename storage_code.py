from os import makedirs
from os.path import join, dirname, exists
from time import time

from get_c_asset import get_program_file_name_from_order

def storage_code(code, username, order_of_program, timestamp = str(time())):
    program_file_name = get_program_file_name_from_order(order_of_asset=order_of_program)
    if program_file_name == None:
        return ''
    code_dir = join(dirname(__file__), "..", "data", "codes", username, program_file_name)
    if not exists(code_dir):
        makedirs(code_dir)
    code_path = join(code_dir, timestamp  + ".c")
    with open(code_path, mode="a", newline="\n") as f:
        f.write(code)
        f.close()

