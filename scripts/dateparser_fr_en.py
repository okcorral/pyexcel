import dateparser
import pandas as pd, openpyxl
from openpyxl import load_workbook

# read in Excel sheet
wb = load_workbook(r'C:\Users\Carol\Dropbox\GECForest_Database\survey_data\COG\COG_Ndoki\normalized\COG_Ndoki_normalized.xlsx', data_only=True)

# load worksheet containing raw dates into memory
wb.worksheets
ws = wb["Missions"]
ws

# define data
data = ws.values

# define columns
cols = next(data)

# read as pandas df
df = pd.DataFrame(data, columns=cols)

# encode as UTF-8
sd_series = df['start_date']
sd_series.str.encode(encoding="utf-8")

ed_series = df['end_date']
ed_series.str.encode(encoding="utf-8")
type(ed_series)

# TODO: ensure there are no None or Null values

# parse and translate datetime field
p_start_date = [dateparser.parse(x).date() for x in sd_series]
p_end_date = [dateparser.parse(x).date() for x in ed_series]

# assign data to specific fields
p_df = df.assign(start_date = p_start_date, end_date = p_end_date)

# save to file
dest_filename = r"C:\code\pyexcel\worksheets\parsed_data.xlsx"
dest_sheetname = 'parsed_by_python' #'Missions_parsed'

# used pandas.DataFrame.to_excel to write DataFrame to an excel sheet
p_df.to_excel(excel_writer=dest_filename, sheet_name=dest_sheetname)
#TODO: ensure this adds new sheet each time it is run

# manually inspect and copy to original Excel spreadsheet