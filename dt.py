import datetime
import re

date = datetime.datetime.now()
dt_str =date.strftime('%Y/%m/%d %H:%M:%S')
dt_str = re.sub(r'[/:\s]',"",dt_str)
print(dt_str)           