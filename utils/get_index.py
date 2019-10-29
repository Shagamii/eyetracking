def get_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default 
