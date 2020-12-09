import os
from datetime import datetime

year = datetime.now().year

for i in range(1,26):
    directory = '{}/Day{:02}'.format(year, i)
    if not os.path.exists(directory):
        os.makedirs(directory)
    #print(directory)
