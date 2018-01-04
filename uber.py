my_table = [[1,2,534,6],[2,346,999,774,354],[3,84,0,774],[4,463,0,212,999]]

def max_col(table):
    i = 0
    table_max_number = 0
    while i < len(table):
        if max(table[i]) > table_max_number:
            table_max_number = max(table[i])
            column_max_number = (1+(table[i].index(max(table[i]))))
            i += 1
        else:
            i += 1
    return column_max_number

print (max_col(my_table))
