# Задача №1

orbits = [(1, 3), (2.5, 10), (7, 2), (6,6), (4, 10)]
def find_farthest_orbit(orbits):
    return max(orbits, key=lambda x:(x[0]!=x[1])*x[0]*x[1])
print(find_farthest_orbit(orbits))



# Задача №2

def same_by(characteristic, objects):
    some_list = list(filter(characteristic, objects))
    print(some_list)
    return len(some_list) == len(objects) or len(some_list) == 0

values = [0, 2, 10, 6]
print((same_by(lambda x: x % 2, values)))




# Задача №3

def print_operation_table(operation, num_rows=9, num_columns=9):
    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            print(operation(row, col), end='\t')
        print()

print('Таблица умножения:')
print_operation_table(lambda x, y: x * y)
print(5*'---')
print('Таблица сложения:')
print_operation_table(lambda x, y: x + y)
