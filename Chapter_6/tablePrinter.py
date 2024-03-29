tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(t):
    table_size = len(t)
    colWidths = [max([len(t[i][k]) for k in range(len(t[i]))]) for i in range(len(t))]
    for i in range(len(t[0])):
        for k in range(table_size):
            if k == table_size - 1:
                print(t[k][i].rjust(colWidths[k]), end='\n')
            else:
                print(t[k][i].rjust(colWidths[k]), end=' ')
    
printTable(tableData)
