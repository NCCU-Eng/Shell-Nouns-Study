import pandas as pd

df = pd.read_csv("../corpus/shell_noun.csv")

with open('../corpus/shell_noun.json', 'w', encoding='utf-8') as file:
    df.to_json(file, force_ascii=False)

print("shell_noun.json ready!")
