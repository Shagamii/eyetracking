def get_correct_time_stamp(time_stamp, start_time, initial_time_stamp):
    return start_time.timestamp() + (time_stamp - initial_time_stamp)/1000000