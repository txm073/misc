import pandas as pd
import numpy as np
from tabula.table import read_pdf_table
import PyPDF2

path = r"C:\Users\Tom\Downloads\Final Student List 22-23.pdf"
reader = PyPDF2.PdfFileReader(open(path, mode='rb'))
m = reader.getNumPages()
#print(reader)
print(m)
for i in range(m):
    n = i+1

    if n==1:
        df = read_pdf_table(path, pandas_options={'header': None, 'error_bad_lines': False}, pages=n)
        index = np.where(df[0].isnull())[0]
        sect = df.iloc[index[0]:index[-1]]
        s = []
        headers = []
        for col in sect:
            colnames = sect[col].dropna().values.flatten()
            (s.insert(len(s), colnames))
            pic = [' '.join(s[col])]
            for i in pic:
                headers.append(i)
        print(df)
        df.drop(sect, inplace=True)
        df.columns = headers
        new_df = pd.DataFrame(columns=headers)
        new_df = pd.concat([new_df, df], axis=0, ignore_index=True)

    else:
        df_2 = read_pdf_table(path, pandas_options={'header': None, 'error_bad_lines': False, 'encoding': "ISO-8859-1"}, pages=n)
        df_2.drop(sect, inplace=True)
        df_2.columns = headers
        new_df = pd.concat([new_df, df_2], axis=0, ignore_index=True)

new_df.columns = headers