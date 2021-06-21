import pandas as pd

# https://www.cisco.com/c/en/us/td/docs/security/wsa/wsa11-7/user_guide/b_WSA_UserGuide_11_7/b_WSA_UserGuide_11_7_chapter_01001.html
excel = pd.read_excel('input_excel.xlsx', sheet_name='mappings', index_col='Cisco_Category_Code', na_values=['NA'])
#csv = pd.read_excel('input_csv.csv', sheet_name='mappings', index_col='Cisco_Category_Code', na_values=['NA'])

print(excel)
print(excel.loc[1006,'Palo_01_Category'])
try:
    print(excel.loc[1006,'Palo_02_Category'])
except KeyError:
    print("Oops!  2nd Palo category for %s not defined. Try again..." % (excel.loc[1006,'Cisco_Category_Name']))