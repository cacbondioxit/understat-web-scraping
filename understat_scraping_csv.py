from bs4 import BeautifulSoup
import csv

with open("EPL table 21-22 html.txt", "r", encoding='UTF8') as f1:
    text = f1.read()

html = BeautifulSoup(text, "html.parser")

list = html.find_all("td", class_="align-right")
team_list = html.find_all("a")

with open("EPL table 21-22.csv", "w", encoding="utf8", newline="") as f2:
    thewriter = csv.writer(f2)
    header = ['No', 'Team', 'M', 'W', 'D', 'L', 'G', 'GA', 'PTS', 'xG', 'xGA', 'xPTS']
    thewriter.writerow(header)
    num_col = len(header)

    for i in range(20):
        row = []
        row_data = list[i*(num_col-1):(i+1)*(num_col-1)]
        for data in row_data:
            text = data.text
            if "-" in text:
                text = text.split("-")[0]
            elif "+" in text:
                text = text.split("+")[0]
            # text = int(text)
            row.append(text)
        row.insert(1, team_list[i].text)
        thewriter.writerow(row)

        