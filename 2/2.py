"""
Логическая функция F задаётся выражением (¬z)∧x.

| ??? | ??? | ??? | F
| 0   | 0   | 0   | 0
| 0   | 0   | 1   | 1
| 0   | 1   | 0   | 0
| 0   | 1   | 1   | 1
| 1   | 0   | 0   | 0
| 1   | 0   | 1   | 0
| 1   | 1   | 0   | 0
| 1   | 1   | 1   | 0

"""

for z in range(2):
    for y in range(2):
        for x in range(2):
            F = not z and x
            if F:
                print(z, y, x, 1)
            else:
                print(z, y, x, 0)