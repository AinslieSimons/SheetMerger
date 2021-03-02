print('importing pandas...')
import pandas as pd

print('reading Excel file...')
df = pd.read_excel('merge.xlsx', sheet_name=None)
print('\n')

sheet1 = df['Sheet1'].set_index(['ID'])
sheet2 = df['Sheet2'].set_index(['ID'])

print('top of sheet1:')
print(sheet1.head())
print('\n')
print('top of sheet2:')
print(sheet2.head())

merged_sheet = sheet1.join(sheet2, how='outer')
print('\n')
print('top of merged_sheet:')
print(merged_sheet.head())

print('\n')
print('saving merged_sheet...')
merged_sheet.to_excel('merged_sheet.xlsx')
print('...')
print('successfully saved merged_sheet...')
