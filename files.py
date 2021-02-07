import os
import pandas as pd
def JoinFile(fname,files):
    df_total = pd.DataFrame()
    for f in files:         
        file=os.path.join(str(fname),str(f))              # loop through Excel files
        print(file)
        if file.endswith('.xls') or file.endswith(".xlsx"):
            excel_file = pd.ExcelFile(file)
            sheets = excel_file.sheet_names
            for sheet in sheets:               # loop through sheets inside an Excel file
                df = excel_file.parse(sheet_name = sheet)
                df_total = df_total.append(df)

    return df_total
    #df_total.to_excel('combined_file.xlsx')