print("Sivapriya Rajan")
print("SJC21MCA-2042")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("iris.csv")
iris = sns.load_dataset("iris")
plot=sns.displot(data=iris, kde=True)
plt.show()
plot=sns.relplot(iris)
plt.show()
plot=sns.histplot(iris)
plt.show()