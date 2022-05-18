import xlrd

def read_objects(sheetname):
    workbook = xlrd.open_workbook('.Objects.xlsx/')
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()     # rows is a generator object
    headers = next(rows)        # skipping the first row which is headers
    # Dictionary Comprehension
    return { row[0].value: (row[1].value, row[2].value)  for row in rows }

def read_headers(sheetname, testcase):
    workbook = xlrd.open_workbook("./TestData.xlsx")
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    for rowno, row in enumerate(rows):
        if row[0].value == testcase:
            temp_data = worksheet.row_values(rowno-1, start_colx=2)
            data = [ item for item in temp_data if item]    
            return ','.join(data)
            break

def read_data(sheetname, testcase):
    workbook = xlrd.open_workbook("./TestData.xlsx")
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    final_data = [ ]
    for rowno, row in enumerate(rows):
        if row[0].value == testcase:
            temp_data = worksheet.row_values(rowno, start_colx=1)
            data = [ item for item in temp_data if item]
            if data[0] == "Yes":
                final_data.append(tuple(data[1:]))
    return final_data