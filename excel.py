from xlrd import open_workbook
item="134.0"
book = open_workbook('69501376_1526104751479.xls')
print("start1")
for sheet in book.sheets():
    print("start2")
    for rowidx in range(sheet.nrows):
        #print("start3")
        row = sheet.row(rowidx)
        for colidx, cell in enumerate(row):
            #print(cell.value)
            #print("---------------------------------------------------")
            if cell.value == "Date" :
                print(sheet.name)
                print(colidx)
                print(rowidx)
            