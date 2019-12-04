from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from TreeStuff import TaskTree
from Solution import Solution


def label_trees(tree_list, labels):
    def func(ordering):   return list(map(lambda x: labels[x], ordering))

    new_tree_list = []
    for preo, ino in tree_list:
        new_tree_list.append((func(preo), func(ino)))

    return new_tree_list


def file2nodes(filename):
    nodes = []
    with open(filename, 'rt') as f:
        for line in f:
            nodes.append(line)
    return nodes


def file2trees(filename):
    trees = []
    with open(filename, 'rt') as f:
        while f:
            preo = next(f).strip('pre: ').split(',')
            ino = next(f).strip('in: ').split(',')
            trees.append((preo, ino))
    return trees


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


def make_corpus(treefile, nodefile):
    nodes = file2nodes(nodefile)
    node_dict = kmeans(nodes)

    tree_list = file2trees(treefile)
    labeled_trees = label_trees(tree_list, node_dict)
