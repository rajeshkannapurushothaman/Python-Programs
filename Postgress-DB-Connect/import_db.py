import os
import psycopg2
import xlrd

conn = ''
xlpath = r'H:\FullTextInformation.xlsx'

def main():
    conn = psycopg2.connect(user = "admin",
                            password = "xxxx",
                            host = "us-east-1.rds.amazonaws.com",
                            port = "5432",
                            database = "live")
    cursor = conn.cursor()
    # Print PostgreSQL Connection properties
    print ( conn.get_dsn_parameters(),"\n")

    book = xlrd.open_workbook(xlpath)
    sheet = book.sheet_by_name("Sheet1")
    query = '''INSERT INTO fulltextinformation 
    (uniqueid, session, cite, fulltext, hiddenfullbillno, hiddenlookupbillno, hiddenbillno, errorsifany, createddate, numberofchars) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    basepath = r'H:\FullTextAttachments'
#    missinglist = ''
    for r in range(1, sheet.nrows):
        print('--', str(sheet.cell(r,0).value))
        folder = str(sheet.cell(r,0).value)
        fpath = os.path.join(basepath, folder)
        filetxt = ''
        if os.path.exists(fpath):
            with open(os.path.join(fpath, 'Body-' + folder + '.txt'), "r") as file1:
                filetxt = file1.read()
                file1.close()
            cursor.execute(query, (sheet.cell(r,0).value, sheet.cell(r,1).value, sheet.cell(r,2).value, filetxt, sheet.cell(r,4).value, sheet.cell(r,5).value, sheet.cell(r,6).value, sheet.cell(r,7).value, sheet.cell(r,8).value, sheet.cell(r,9).value))
    cursor.close()

    conn.commit()

    conn.close()

if __name__ == "__main__":
    main()