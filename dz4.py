import os
from collections import defaultdict

import aiohttp


root_dir = aiohttp.__path__[0]
aiohttp_files = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
   for file in files:
       a = 1
       while True:
           a *= 10
           if os.stat(os.path.join(root, file)).st_size <= a:
               aiohttp_files[a] += 1
               break
dicti = {}
for k, v in sorted(aiohttp_files.items()):
    dicti.setdefault(k, v)

print(dicti)
