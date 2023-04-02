def pascal(depth):
    current_row = [1]
    yield current_row

    for _ in range(depth):
        next_row_len = len(current_row) + 1
        next_row = [1 for _ in range(next_row_len)]
        for i in range(1, next_row_len - 1):
            next_row[i] = current_row[i-1] + current_row[i]
        current_row = next_row

        yield current_row


def print_row(row):
    for i in range(len(row)):
        print(f'{row[i]:>3} ', end='')
    print('\n')


i = 0
n = 9
space = ' ' * n * 2

for row in pascal(n):
    print(f'{i:>2} {sum(row):>2}{space}', end=' ')
    print_row(row)
    i += 1
    space = space[2:]
