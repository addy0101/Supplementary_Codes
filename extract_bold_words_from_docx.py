from docx import *
import pandas as pd

ess_words = []
document = Document('/filepath')
c=0
for para in document.paragraphs:
    for run in para.runs:
        if run.bold:
            ess_words.append(run.text)
            if c%100 ==0:
                print(c/100)
            c+=1


df = pd.DataFrame(columns=['Col_name'])
df['Col_name'] = ess_words
df.to_csv('bold_words.csv')
