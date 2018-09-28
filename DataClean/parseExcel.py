import pandas as pd 
import numpy as np
import pickle
import json

xlsx_file = "Cards Against Humanity.xlsx"
xlFile = pd.ExcelFile(xlsx_file)
raw_df = pd.read_excel(xlFile, sheetname="CAH Main Deck")
columns = raw_df.iloc[2]
raw_df.columns = columns
prompt_cards_df = raw_df.loc[['Prompt']]
response_cards_df = raw_df.loc[['Response']]
single_prompt_cards = list(prompt_cards_df[prompt_cards_df['Special'].isnull()]['Cards Against Humanity: Main Deck'])
single_response_cards = list(response_cards_df[response_cards_df['Special'].isnull()]['Cards Against Humanity: Main Deck'])

prompt_cards_file = open('prompt_cards.txt', 'w')
json.dump(single_prompt_cards, prompt_cards_file)
prompt_cards_file.close()

response_cards_file = open('response_cards.txt', 'w')
json.dump(single_response_cards, response_cards_file)
response_cards_file.close()

with open('prompt_cards_b', 'wb') as f:
    pickle.dump(single_prompt_cards, f)
with open('response_cards_b', 'wb') as f:
    pickle.dump(single_response_cards, f)