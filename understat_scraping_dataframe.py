from bs4 import BeautifulSoup
import csv
import pandas as pd

with open("EPL table 21-22 html.txt", "r", encoding='UTF8') as f:
    text = f.read()

html = BeautifulSoup(text, "html.parser")

list = html.find_all("td", class_="align-right")
team_list = html.find_all("a")

header = ['No', 'Team', 'M', 'W', 'D', 'L', 'G', 'GA', 'PTS', 'xG', 'xGA', 'xPTS']
num_col = len(header)

data_list = []
for i in range(20):
    row = []
    row_data = list[i*(num_col-1):(i+1)*(num_col-1)]
    for data in row_data:
        text = data.text
        if "-" in text:
            text = float(text.split("-")[0])
        elif "+" in text:
            text = float(text.split("+")[0])
        else:
            text = int(text)
        row.append(text)
    row.insert(1, team_list[i].text)
    data_list.append(row)

df = pd.DataFrame(data=data_list, columns=header)
print(df)