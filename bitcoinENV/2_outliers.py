import pandas as pd
import matplotlib.pyplot as plt
import seaborn as se

data = pd.read_csv("main.csv")


plt.rcParams['figure.figsize'] = (16,4)
# plt.style.use('fivethirtyeight')


plt.subplot(1,4,1)
se.boxplot(data['Open'])

plt.subplot(1,4,2)
se.boxplot(data['High'])

plt.subplot(1,4,3)
se.boxplot(data['Low'])

plt.subplot(1,4,4)
se.boxplot(data['Close'])


plt.suptitle('checking for univariate outliers')
plt.show()


plt.subplot(1,1,1)
se.scatterplot(y=data['Open'],x=data['High'])

plt.show()