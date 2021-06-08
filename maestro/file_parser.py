import pandas as pd

file = 'Modafinal_Analogue_0212.txt'
labels = ['Name', 'Smile']
df = pd.read_csv(file, names=labels, sep='\t')
for i in range(len(df)):
    with open(df["Name"][i]+'.smi', "w") as f:
        f.write(df["Smile"][i])
