"""
This program uses the math module and the round function to print pi
approximated to different numbers of decimal places.
"""

import math

print [round(math.pi, i) for i in range(1, 6)]