tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


longest_strings = [max([len(tableData[i][k]) for k in range(len(tableData[i]))]) for i in range(len(tableData))]


def printTable(t):
    table_size = len(t)
    colWidths = [max([len(t[i][k]) for k in range(len(t[i]))]) for i in range(len(t))]
    for i in range(len(t[0])):
        for k in range(table_size):
            if k == table_size - 1:
                print(t[k][i].ljust(8), end='\n')
            elif k == 0:
                print(t[k][i].rjust(8), end='')
            else:
                print(t[k][i].center(8), end='')

printTable(tableData)
