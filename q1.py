#
# Name: Lim Yong Yin
# Email ID: yongyin.lim.2018
#
from sys import builtin_module_names


def get_color(code):
    # write your answer below
    code = code.lower()
    if code == 'r':
        return 'Red'
    if code == 'g':
        return "Green"
    if code == 'b':
        return 'Blue'
    
    return "Invalid"

    