import csv
from os.path import join, dirname, exists
from os import makedirs

HEADER_OF_LAYOUT = [
    "key",
    'x',
    'y',
    'width',
    'height'
]

KEY_OF_LAYOUT = [
    "page",
    "header",
    "editor",
    "editorRow",
    "executor",
    "terminal",
    "question"
]

def storage_layout(layout, _path):
    csv_dir = join(dirname(__file__), "..", "data", "layout")
    if not exists(csv_dir):
        makedirs(csv_dir)
    csv_path = join(csv_dir, _path + ".csv")
    with open(csv_path, 'w', newline="") as f:
        writer = csv.DictWriter(f, HEADER_OF_LAYOUT)
        writer.writeheader()
        writer.writerows(layout)
