print("Sivapriya Rajan")
print("SJC21MCA-2042")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("iris.csv")
iris = sns.load_dataset("iris")
plot=sns.pairplot(iris,kind="hist", markers=["s"])
plot=sns.pairplot(iris,kind="kde",markers=["D"])
plot=sns.pairplot(iris,kind="scatter")
plot=sns.pairplot(iris,kind="reg",markers=["o"])
plt.show()