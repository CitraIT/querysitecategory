######################################################################
# Citra IT - Excelencia em TI
# Script para consultar API de categorização de website do FortiGuard
# @Author: luciano@citrait.com.br
# @Version: 0.1
# @Usage: python forticategory.py www.gmail.com
# >>> gmail.com: Web-based Email
######################################################################

import sys
import re
import requests


r = requests.get(f"https://www.fortiguard.com/webfilter?q={sys.argv[1]}")
c = re.compile('<h4 class="info_title">Category: (?P<category>[^<]+)</h4>')
target_category = c.search(r.text).group("category")
print(f'{sys.argv[1]}: {target_category}')
