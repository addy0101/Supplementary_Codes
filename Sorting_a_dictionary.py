
z = {'lorem':12, 'ipsum':1, 'is':6, 'simply':2}
import seaborn
import matplotlib.pyplot as plt
import collections as c

z1 = c.OrderedDict(sorted(z.items(), key= lambda t: t[1], reverse=True))
print(z1)

seaborn.set(style="whitegrid")
fig, ax = plt.subplots()
seaborn.barplot(list(z1.keys()),list(z1.values()),ax=ax)
plt.show()
