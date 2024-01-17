import math
import os
from random import random
import re
import sys

n = 3
notW = "Not Weird"
w = "Weird"

n = int(input().strip())

if (n % 2) == 1:
    print(w)
elif (n % 2) == 0 and n in range(2,5):
    print(notW)
elif (n % 2) == 0 and n in range(6,21):
    print(w)
elif (n % 2) == 0 and n > 20:
        print(notW)
else:
    None