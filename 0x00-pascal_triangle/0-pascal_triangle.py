"""Function pascal triangle"""


def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = [[1]]
    for i in range(1, n):
        prev_row = pascal[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        pascal.append(new_row)

    return pascal
