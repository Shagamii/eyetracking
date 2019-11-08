import csv
from os.path import join, dirname, exists
from os import mkdir

HEADER_OF_LAYOUT = [
    "page",
    "header",
    "editor",
    "editorRow",
    "executor",
    "terminal"
]


def storage_layout(layout, _path):
    csv_dir = join(dirname(__file__), "..", "data", "layout")
    if not exists(csv_dir):
        mkdir(csv_dir)
    csv_path = join(csv_dir, _path + ".csv")
    with open(csv_path, 'w', newline="") as f:
        writer = csv.DictWriter(f, HEADER_OF_LAYOUT)
        writer.writerow(layout)
