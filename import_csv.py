import csv
from os.path import join, dirname

def import_csv(_path, selector=None):
    csv_path = join(dirname(__file__), "..", "data" , _path + ".csv")
    with open(csv_path) as f:
        reader = csv.reader(f)
        return [selector(row) for row in reader]