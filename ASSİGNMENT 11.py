import pandas
import requests

# Define the remote file to retrieve
        # BURAYA EXCEL DOSYASININ LİNKİ GELECEK
remote_url = "https://go.microsoft.com/fwlink/?LinkID=521962"

# Define the local filename to save data
local_file = 'local_copy.xlsx'
# Make http request for remote file data
data = requests.get(remote_url)
# Save file data to local copy
with open(local_file, 'wb') as file:
    file.write(data.content)

excel_data_hami = pandas.read_excel("local_copy.xlsx")
#df = excel_data_hami.parse("Sheet1")


colums = excel_data_hami.columns.ravel()

Years = excel_data_hami[colums[0]].tolist()
Unemployement = excel_data_hami[colums[1]].tolist()
Inflation = excel_data_hami[colums[2]].tolist()
Interestrate = excel_data_hami[colums[3]].tolist()
GDPpercapitagrowth = excel_data_hami[colums[4]].tolist()

df = pandas.DataFrame({colums[1]: Unemployement,
                       colums[2]: Inflation,
                       colums[3]: Interestrate,
                       colums[4]: GDPpercapitagrowth},
                    index=Years)

df["HAMI"] = df[colums[1]] + df[colums[2]] + df[colums[3]] - df[colums[4]]

df = df.drop(columns = [colums[1], colums[2], colums[3], colums[4]])

df.to_excel("AssıgnAlpERENOKUR.xls")