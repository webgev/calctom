class ErrorPrice(Exception):
    pass
class ErrorCount(Exception):
    pass

class ErrorState(Exception):
    pass
    

DISCOUNTS = {
    range(0, 1000): 0,
    range(1000, 5000): 3,
    range(5000, 7000): 5,
    range(7000, 10000): 7,
    range(10000, 50000): 10,
}

STATE = {
    'ut': 6.85,
    'nv': 8,
    'tx': 6.25,
    'al': 4,
    'ca': 8.25,
}

MAX_DISCOUNTS = 15

def valid_int(value):
    return value and (isinstance(value, float) or isinstance(value, int) or (str(value).isdigit() and float(value) > 0))