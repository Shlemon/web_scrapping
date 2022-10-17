import pandas as pd
import numpy as np


class DataGen:
    def __init__(self):
        self.dataframe = pd.read_csv('./exported.csv')
        self.cleaned_df = []

        self.split()
        self.save_to_csv()

    def split(self):
        for index, row in self.dataframe.iterrows():
            words = np.char.split(row['text'])
            labels = row['tags']
            self.cleaned_df.append(
                {'words': words, 'label': labels}
            )
    
    def save_to_csv(self):
        df = pd.DataFrame(data=self.cleaned_df, 
             columns=pd.Series(data=['words', 'label']))
        df.to_csv(path_or_buf='./cleaned_export.csv')