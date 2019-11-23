from os import makedirs
from os.path import join, dirname, exists
from time import time

def storage_code(code, username, order_of_program, timestamp = str(time())):
    code_dir = join(dirname(__file__), "..", "data", "codes", username, str(order_of_program))
    if not exists(code_dir):
        makedirs(code_dir)
    code_path = join(code_dir, timestamp  + ".c")
    with open(code_path, mode="a") as f:
        f.write(code)
        f.close()

