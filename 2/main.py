def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        print()
        for j in range(1, num_columns + 1):
            print(operation(i, j), end="\t")


num_rows = int(input("Enter number of rows: "))
num_columns = int(input("Enter number of columns: "))
print("Result :")
print_operation_table(lambda x, y: x * y, num_rows, num_columns)
