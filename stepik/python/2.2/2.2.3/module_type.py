import check
import sys

print('Type: ', type(check))
# print(sys.modules) # видим модуль check наряду со встроенными
print('ID: ', id(check))

import check
print('ID: ', id(check))
