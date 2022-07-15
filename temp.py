# Структура A:
#
# Поле	Описание
# 1	Адрес (uint16) структуры B
# 2	uint64
# 3	int32
# 4	uint16
# 5	int32
# 6	Структура D
# 7	float

from struct import *
packed_data = pack("<iif", 1, 2, 3.4)
print(packed_data)