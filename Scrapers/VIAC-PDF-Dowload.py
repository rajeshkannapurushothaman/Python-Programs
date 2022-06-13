import requests
import tabula
res=requests.get('https://www.xxxxxxxxx.it/appointed.pdf')
with open('testing.pdf','wb') as f:
    f.write(res.content)
tabula.convert_into("testing.pdf", "testing.csv", output_format="csv", pages='all')
#tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')  -> for multiple pdfs in a directory
