import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np


def main():
    features = ['sleep quality', 'social interaction', 'exercise', 'goals satisfaction', 'stress']
    target = ['mood']
    features_abbrev = {'sleep quality': 'sq','social interaction': 'si','exercise': 'e','goals satisfaction': 'gs','stress': 's'}

    df = pd.read_csv("mock.csv")
    x = df.loc[:, features].values
    x = StandardScaler().fit_transform(x)  # mean 0 and variance 1

    # PCA
    pca = PCA(n_components=2)
    prcomp = pca.fit_transform(x)
    prcomp_df = pd.DataFrame(data=prcomp, columns=['PC1', 'PC2'])
    combined_df = pd.concat([prcomp_df, df[target]], axis=1)
    components = pca.components_
    variance_ratios_list = pca.explained_variance_ratio_
    total_variance_percentage = sum(variance_ratios_list) * 100
    print("Explained variances:")
    print(variance_ratios_list)

    fig, ax = plt.subplots()
    fig.set_size_inches(13, 10)

    ax.set_xlabel('PC1', fontsize=15)
    ax.set_ylabel('PC2', fontsize=15)
    title = '2D projection Summary.' + '\n' + 'Explained Variance: ' + \
            "{:.0f}".format(total_variance_percentage) + ' % from Total.'
    ax.set_title(title, fontsize=20)

    colors = combined_df['mood'].tolist()

    plt.scatter(combined_df['PC1'], combined_df['PC2'], c=colors, cmap='plasma_r', s=80)
    cbar = plt.colorbar()
    cbar.set_label('Mood')

    # Plotting the vectors corresponding to the original features
    V = components.T

    for i in range(len(V)):
        V[i] = V[i] / np.linalg.norm(V[i])

    origin = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    plt.quiver(*origin, V[:, 0], V[:, 1], color=['k'], scale=1, scale_units='xy', width=0.003)

    xs = V[:, 0]
    ys = V[:, 1]

    for i, (x, y) in enumerate(zip(xs, ys)):
        label = features_abbrev[features[i]]
        plt.annotate(label, (x, y), textcoords="offset points", xytext=(5 * x, 5 * y), ha='center')

    plt.savefig("plot.png")


if __name__ == "__main__":
    main()
