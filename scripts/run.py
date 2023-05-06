import pandas as pd
from bs4 import BeautifulSoup

df_ge = pd.read_csv("../corpus/shell noun_GER.csv")

with open("../corpus/shell_noun.html", "r") as f:
    html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    # find table header in soup
    col_names = [x.text for x in soup.find_all("thead")[0].find_all("th")]
    rows = [[y.text for y in x.find_all("td")] for x in soup.find_all("tbody")[
        0].find_all("tr")]

    df_online = pd.DataFrame(rows, columns=col_names[1:])

print(df_online.shape)
df_online['trans_Deutsch'] = ""
df_online['sent_Deutsch'] = ""

for idy, rov in df_online.iterrows():
    for idx, row in df_ge.iterrows():
        if rov['Cate-1'] == row['Class'] and rov['Cate-2'] == row['Group'] and rov['Cate-3'] == row['shell_nouns']:
            # trans_d.append((idy, row['德文翻譯']))
            # sent_d.append((idy, row['德文例句']))
            df_online.at[idy, 'trans_Deutsch'] = row['德文翻譯']
            df_online.at[idy, 'sent_Deutsch'] = row['德文例句']


# replace pandas nan with empty string
df_online = df_online.fillna("")

new_order = ['Cate-1', 'Cate-2', 'Cate-3', 'trans_Czech', 'trans_Japan',
       'trans_English', 'trans_Vienamese', 'trans_Deutsch', 'sent_Vienamese', 'sent_English',
       'sent_Japan', 'sent_Czech', 'sent_Chinese', 
       'sent_Deutsch']
with open('../corpus/shell_noun2.html', 'w', encoding='utf-8') as file:
    df_online[new_order].to_html(file)
