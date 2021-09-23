import pandas as pd

#df = pd.DataFrame({'MSSV':[18110321,18110326],'HoVaTen':['Nam','Nghia']})

#df.to_excel('./hello.xlsx', sheet_name='States', index=False)

df = pd.read_excel('hello.xlsx')
print(df.to_dict(orient='record'))