tuple1 = (11, 22)
tuple2 = (99, 88)
temp = tuple1
tuple1 = tuple2
tuple2 = temp
print(f'tuple1: {tuple1}')
print(f'tuple2: {tuple2}')