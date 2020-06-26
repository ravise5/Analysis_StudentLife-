import pandas as pd
import matplotlib as plt
import seaborn as sns
df = pd.read_csv("Stress.csv")
'''
corr = df.corr()
corr = corr['Stress Level']
print(corr)

df.plot.scatter(x='Stress Level',y='Social')
'''

corrmat = df.corr()
top_corr_features = corrmat.index
#plt.figure(figsize=(12,12))
g=sns.heatmap(df[top_corr_features].corr(),annot=True,cmap="RdYlGn",square=True)
g.set_xticklabels(
    g.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);
b, t = plt.ylim() # discover the values for bottom and top
b += 0.5 # Add 0.5 to the bottom
t -= 0.5 # Subtract 0.5 from the top
plt.ylim(b, t) # update the ylim(bottom, top) values
plt.show() # ta-da!



