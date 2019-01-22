tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'tigers', 'goose']]

def printTable(tableData):
    colWidths= []
    for i in tableData:
        length = 0
        for item in i:
            if len(item) > length:
                length = len(item)
#        print("Longest is", length)
        colWidths.append(length)

    largestWidth = max(colWidths)
    print(largestWidth)



    print(tableData.rjust(largestWidth))






printTable(tableData)
