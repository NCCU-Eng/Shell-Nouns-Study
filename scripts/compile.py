import pandas as pd

df = pd.read_csv("../corpus/shell_noun.csv")
df.columns = ['cate1', 'cate2', 'cate3', 'trans_ch', 'trans_jp', 'trans_cz', "sent_eng", "sent_jp", "sent_cz", "sent_ch"]

with open('../corpus/shell_noun.json', 'w', encoding='utf-8') as file:
    df.to_json(file, force_ascii=False)

print("shell_noun.json ready!")
