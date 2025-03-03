import pandas as pd
df = pd.read_csv("fashion-mnist_test.csv")
X = df.iloc[:, 1:]
y = df.iloc[:, :1]
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)
pca.explained_variance_ratio_
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

fig, axarr = plt.subplots(1, 2, figsize=(12, 4))

sns.heatmap(pca.components_[0, :].reshape(28, 28), ax=axarr[0], cmap='gray_r')
sns.heatmap(pca.components_[1, :].reshape(28, 28), ax=axarr[1], cmap='gray_r')
axarr[0].set_title(
    "{0:.2f}% Explained Variance".format(pca.explained_variance_ratio_[0]*100),
    fontsize=12
)
axarr[1].set_title(
    "{0:.2f}% Explained Variance".format(pca.explained_variance_ratio_[1]*100),
    fontsize=12
)
axarr[0].set_aspect('equal')
axarr[1].set_aspect('equal')

plt.suptitle('2-Component PCA')
pca = PCA(n_components=4)
X_r = pca.fit(X).transform(X)

import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

fig, axarr = plt.subplots(2, 2, figsize=(12, 8))

sns.heatmap(pca.components_[0, :].reshape(28, 28), ax=axarr[0][0], cmap='gray_r')
sns.heatmap(pca.components_[1, :].reshape(28, 28), ax=axarr[0][1], cmap='gray_r')
sns.heatmap(pca.components_[2, :].reshape(28, 28), ax=axarr[1][0], cmap='gray_r')
sns.heatmap(pca.components_[3, :].reshape(28, 28), ax=axarr[1][1], cmap='gray_r')

axarr[0][0].set_title(
    "{0:.2f}% Explained Variance".format(pca.explained_variance_ratio_[0]*100),
    fontsize=12
)
axarr[0][1].set_title(
    "{0:.2f}% Explained Variance".format(pca.explained_variance_ratio_[1]*100),
    fontsize=12
)
axarr[1][0].set_title(
    "{0:.2f}% Explained Variance".format(pca.explained_variance_ratio_[2]*100),
    fontsize=12
)
axarr[1][1].set_title(
    "{0:.2f}% Explained Variance".format(pca.explained_variance_ratio_[3]*100),
    fontsize=12
)
axarr[0][0].set_aspect('equal')
axarr[0][1].set_aspect('equal')
axarr[1][0].set_aspect('equal')
axarr[1][1].set_aspect('equal')

plt.suptitle('4-Component PCA')
pass


import numpy as np

pca = PCA(n_components=10)
X_r = pca.fit(X).transform(X)

plt.plot(range(10), pca.explained_variance_ratio_)
plt.plot(range(10), np.cumsum(pca.explained_variance_ratio_))
plt.title("Component-wise and Cumulative Explained Variance")
pass
from sklearn.preprocessing import normalize 
X_norm = normalize(X.values)


from sklearn.decomposition import PCA

pca = PCA(n_components=120)
X_norm_r = pca.fit(X_norm).transform(X_norm)
sns.heatmap(pd.DataFrame(X_norm).mean().values.reshape(28, 28), cmap='gray_r')
sns.heatmap(pd.DataFrame(X).std().values.reshape(28, 28), cmap='gray_r')
def reconstruction(X, n, trans):
    
    vectors = [trans.components_[n] * X[n] for n in range(0, n)]
    
    
    ret = trans.inverse_transform(X)


    ret[ret < 0] = 0
    ret[ret > 1] = 1
    return ret
fig, axarr = plt.subplots(1, 2, figsize=(12, 4))

sns.heatmap(X_norm[0, :].reshape(28, 28), cmap='gray_r',
            ax=axarr[0])
sns.heatmap(reconstruction(X_norm_r[0, :], 120, pca).reshape(28, 28), cmap='gray_r',
            ax=axarr[1])
axarr[0].set_aspect('equal')
axarr[0].axis('off')
axarr[1].set_aspect('equal')
axarr[1].axis('off')
def n_sample_reconstructions(X, n_samples=5, trans_n=120, trans=None):
    
    sample_indices = np.round(np.random.random(n_samples)*len(X))
    return (sample_indices, 
            np.vstack([reconstruction(X[int(ind)], trans_n, trans) for ind in sample_indices]))


def plot_reconstructions(X, n_samples=5, trans_n=120, trans=None):
   
    fig, axarr = plt.subplots(n_samples, 3, figsize=(12, n_samples*4))
    ind, reconstructions = n_sample_reconstructions(X, n_samples, trans_n, trans)
    for (i, (ind, reconstruction)) in enumerate(zip(ind, reconstructions)):
        ax0, ax1, ax2 = axarr[i][0], axarr[i][1], axarr[i][2]
        sns.heatmap(X_norm[int(ind), :].reshape(28, 28), cmap='gray_r', ax=ax0)
        sns.heatmap(reconstruction.reshape(28, 28), cmap='gray_r', ax=ax1)
        sns.heatmap(np.abs(X_norm[int(ind), :] - reconstruction).reshape(28, 28), 
                    cmap='gray_r', ax=ax2)
        ax0.axis('off')
        ax0.set_aspect('equal')
        ax0.set_title("Original Image", fontsize=12)
        ax1.axis('off')
        ax1.set_aspect('equal')
        ax1.set_title("120-Vector Reconstruction", fontsize=12)
        ax2.axis('off')
        ax2.set_title("Original-Reconstruction Difference", fontsize=12)
        ax2.set_aspect('equal')
        plot_reconstructions(X_norm_r, n_samples=10, trans_n=120, trans=pca)
from sklearn.metrics import mean_squared_error

def quartile_record(X, vector, q=0.5):
   
    errors = [mean_squared_error(X_norm[i, :], vector) for i in range(len(X_norm))]
    errors = pd.Series(errors)
    
    e_value = errors.quantile(q, interpolation='lower')
    return X[errors[errors == e_value].index[0], :]
def plot_quartile_reconstructions(X, n_samples)
def plot_quartiles(X, trans, n):

    fig, axarr = plt.subplots(n, 7, figsize=(12, n*2))
    for i in range(n):
        vector = trans.components_[i, :]
        sns.heatmap(quartile_record(X, vector, q=0.02).reshape(28, 28), 
            cmap='gray_r', ax=axarr[i][0], cbar=False)
        axarr[i][0].set_aspect('equal')
        axarr[i][0].axis('off')
        
        sns.heatmap(quartile_record(X, vector, q=0.1).reshape(28, 28), 
            cmap='gray_r', ax=axarr[i][1], cbar=False)
        axarr[i][1].set_aspect('equal')
        axarr[i][1].axis('off')
        
        sns.heatmap(quartile_record(X, vector, q=0.25).reshape(28, 28), 
            cmap='gray_r', ax=axarr[i][2], cbar=False)
        axarr[i][2].set_aspect('equal')
        axarr[i][2].axis('off')
        
        sns.heatmap(quartile_record(X, vector, q=0.5).reshape(28, 28), 
            cmap='gray_r', ax=axarr[i][3], cbar=False)
        axarr[i][3].set_aspect('equal')
        axarr[i][3].axis('off')

        sns.heatmap(quartile_record(X, vector, q=0.75).reshape(28, 28), 
            cmap='gray_r', ax=axarr[i][4], cbar=False)
        axarr[i][4].set_aspect('equal')
        axarr[i][4].axis('off')

        sns.heatmap(quartile_record(X, vector, q=0.9).reshape(28, 28), 
            cmap='gray_r', ax=axarr[i][5], cbar=False)
        axarr[i][5].set_aspect('equal')
        axarr[i][5].axis('off')        
        
        sns.heatmap(quartile_record(X, vector, q=0.98).reshape(28, 28), 
            cmap='gray_r', ax=axarr[i][6], cbar=False)        
        axarr[i][6].set_aspect('equal')
        axarr[i][6].axis('off')
        
    axarr[0][0].set_title('2nd Percentile', fontsize=12)
    axarr[0][1].set_title('10th Percentile', fontsize=12)
    axarr[0][2].set_title('25th Percentile', fontsize=12)
    axarr[0][3].set_title('50th Percentile', fontsize=12)
    axarr[0][4].set_title('75th Percentile', fontsize=12)
    axarr[0][5].set_title('90th Percentile', fontsize=12)
    axarr[0][6].set_title('98th Percentile', fontsize=12)
    plot_quartiles(X_norm, pca, 8)
    def record_similarity(X, vector, metric=mean_squared_error):
    
    return pd.Series([mean_squared_error(X_norm[i, :], vector) for i in range(len(X_norm))])
fig, axarr = plt.subplots(2, 4, figsize=(12, 6))
axarr = np.array(axarr).flatten()

for i in range(0, 8):
    record_similarity(X_norm, pca.components_[i]).plot.hist(bins=50, ax=axarr[i])
    axarr[i].set_title("Component {0} Errors".format(i + 1), fontsize=12)
    axarr[i].set_xlabel("")
    axarr[i].set_ylabel("")
    
    
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X_r)
# Visualize t-SNE results
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_tsne[:, 0], y=X_tsne[:, 1], hue=y.values.ravel(), palette='tab10', s=60, edgecolor='k', alpha=0.7)
plt.title("t-SNE visualization of PCA-reduced data", fontsize=16)
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.legend(title="Labels")
plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import normalize


df = pd.read_csv("fashion-mnist_test.csv")
X = df.iloc[:, 1:]
y = df.iloc[:, :1]


X_norm = normalize(X.values)


pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)


fig, axarr = plt.subplots(1, 2, figsize=(12, 4))
sns.heatmap(pca.components_[0, :].reshape(28, 28), ax=axarr[0], cmap='gray_r')
sns.heatmap(pca.components_[1, :].reshape(28, 28), ax=axarr[1], cmap='gray_r')
axarr[0].set_title("{0:.2f}% Explained Variance".format(pca.explained_variance_ratio_[0]*100), fontsize=12)
axarr[1].set_title("{0:.2f}% Explained Variance".format(pca.explained_variance_ratio_[1]*100), fontsize=12)
axarr[0].set_aspect('equal')
axarr[1].set_aspect('equal')
plt.suptitle('2-Component PCA')


tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X_r)

# Visualize t-SNE results
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_tsne[:, 0], y=X_tsne[:, 1], hue=y.values.ravel(), palette='tab10', s=60, edgecolor='k', alpha=0.7)
plt.title("t-SNE visualization of PCA-reduced data", fontsize=16)
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.legend(title="Labels")
plt.show()


pca = PCA(n_components=4)
X_r = pca.fit(X).transform(X)


fig, axarr = plt.subplots(2, 2, figsize=(12, 8))
sns.heatmap(pca.components_[0, :].reshape(28, 28), ax=axarr[0][0], cmap='gray_r')
sns.heatmap(pca.components_[1, :].reshape(28, 28), ax=axarr[0][1], cmap='gray_r')
sns.heatmap(pca.components_[2, :].reshape(28, 28), ax=axarr[1][0], cmap='gray_r')
sns.heatmap(pca.components_[3, :].reshape(28, 28), ax=axarr[1][1], cmap='gray_r')
for i in range(4):
    axarr[i//2][i%2].set_title("{0:.2f}% Explained Variance".format(pca.explained_variance_ratio_[i]*100), fontsize=12)
    axarr[i//2][i%2].set_aspect('equal')
    axarr[i//2][i%2].axis('off')
plt.suptitle('4-Component PCA')


X_r_4 = pca.fit_transform(X)
tsne = TSNE(n_components=2, random_state=42)
X_tsne_4 = tsne.fit_transform(X_r_4)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_tsne_4[:, 0], y=X_tsne_4[:, 1], hue=y.values.ravel(), palette='tab10', s=60, edgecolor='k', alpha=0.7)
plt.title("t-SNE visualization of 4-Component PCA-reduced data", fontsize=16)
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.legend(title="Labels")
plt.show()


