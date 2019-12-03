from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def kmeans(corpus) -> dict:
    vectorizer = TfidfVectorizer(max_features=4)
    X = vectorizer.fit_transform(corpus)

    # cluster
    num_clusters = 3
    km = KMeans(n_clusters=num_clusters)
    km.fit(X)

    # order and get labels
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()

    # make dict
    label_dict = dict()
    for label, doc in zip(km.labels_, corpus):
        label_dict[doc] = label

    return label_dict
