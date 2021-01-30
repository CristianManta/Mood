import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np


# df = pd.read_sql_table('table_name', 'postgres:///db_name')


def main():
    features = ['sleep quality', 'social interaction', 'exercise', 'goals satisfaction', 'stress']
    target = ['mood']

    df = pd.read_csv("mock.csv")
    x = df.loc[:, features].values
    y = df.loc[:, target].values

    x = StandardScaler().fit_transform(x)  # mean 0 and variance 1

    # PCA
    pca = PCA(n_components=2)
    prcomp = pca.fit_transform(x)
    prcomp_df = pd.DataFrame(data=prcomp, columns=['PC1', 'PC2'])
    combined_df = pd.concat([prcomp_df, df[target]], axis=1)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('PC1', fontsize=15)
    ax.set_ylabel('PC2', fontsize=15)
    ax.set_title('2D projection summary', fontsize=20)
    targets = np.arange(11)
    # colors = [[1,2,3], [4,5,6]]
    for target in targets:
        indicesToKeep = combined_df['mood'] == target
        ax.scatter(combined_df.loc[indicesToKeep, 'PC1']
                   , combined_df.loc[indicesToKeep, 'PC2']
                   , c=None
                   , s=50)
    ax.legend(targets)
    ax.grid()
    plt.savefig("plot.png")


if __name__ == "__main__":
    main()
