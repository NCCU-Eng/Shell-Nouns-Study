import pandas as pd

df = pd.read_csv("../corpus/shell_noun.csv")
df.columns = ['cate1', 'cate2', 'cate3', 'trans_ch', 'trans_jp', 'trans_cz', "sent_eng", "sent_jp", "sent_cz", "sent_ch"]
df.fillna('', inplace=True)

with open('../corpus/shell_noun.html', 'w', encoding='utf-8') as file:
    df.to_html(file)

print("shell_noun.html ready!")
