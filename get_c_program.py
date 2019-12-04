from os.path import join, dirname

from get_c_asset import get_c_asset

def get_c_program(order_of_assets):
    return get_c_asset(order_of_asset=order_of_assets, asset_dirname="program")