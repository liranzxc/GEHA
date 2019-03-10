import pandas as pd


file = 'data.xlsx'
pd.set_option('display.max_colwidth', -1) # display enitre coloums
# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names


df1 = xl.parse('גיליון1')

#print(df1)
#print(df1[["Patient","Id_Num","סטטוס חוקי","סיבת האשפוז"]])

#print(df1)
message = (df1[df1["Patient"] == 3320]["Med"])
message = message.to_string()
print(message)
with open("myfile.txt","w",encoding="utf-8") as file:
    for item in message.split(";"):
        file.write(item)
        file.write("\n")



