    """A handy little script to create a directory for the current year's AoC (with sub-folders for each day), if it doesn't already exist.
    """

import os
from datetime import datetime

year = datetime.now().year

for i in range(1,26):
    directory = '{}/D{:02}'.format(year, i)
    if not os.path.exists(directory):
        os.makedirs(directory)
    #print(directory)
