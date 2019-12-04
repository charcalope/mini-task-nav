from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def label_trees(tree_list, labels):
    def func(ordering): return list(map(lambda x: labels[x], ordering))

    new_tree_list = []
    for preo, ino in tree_list:
        new_tree_list.append((func(preo), func(ino)))

    return new_tree_list


def file2nodes(filename):
    nodes = []
    with open(filename, 'rt') as f:
        for line in f:
            nodes.append(line.strip())
    return nodes


def file2trees(filename):
    trees = []
    with open(filename, 'rt') as f:
        while True:
            preo = f.readline().strip().strip('pre:')
            ino = f.readline().strip().strip('in:')

            if not ino:
                break
            l1 = [a.strip() for a in preo.split(',')]
            l2 = [a.strip() for a in ino.split(',')]
            trees.append((l1, l2))
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


def make_corpus(node_file, tree_file):
    nodes = file2nodes(node_file)
    node_dict = kmeans(nodes)
    trees = file2trees(tree_file)
    labeled = label_trees(trees, node_dict)
    return labeled


def test_each():
    print('TESTING TREE READ')
    print('________________________________________')
    test_output = file2trees('test_trees.txt')
    for preo, ino in test_output:
        print(preo)
        print(ino)
        print()
    print()

    print('TESTING NODE READ')
    print('________________________________________')
    test_output = file2nodes('test_nodes.txt')
    for node in test_output:
        print(node)
    print()

    print('TESTING CLUSTERING')
    print('________________________________________')
    nodes = file2nodes('test_nodes.txt')
    node_dict = kmeans(nodes)
    for key, val in node_dict.items():
        print(f'{key}: {val}')
    print()

    print('TESTING LABELING')
    print('________________________________________')
    trees = file2trees('test_trees.txt')
    labeled = label_trees(trees, node_dict)
    for preo, ino in labeled:
        print(preo)
        print(ino)
        print()
    print()

