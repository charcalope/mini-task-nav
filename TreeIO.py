from Solution import Solution
from TaskTree import TaskTree

class TreeIO:
    def __init__(self):
        self.dict = dict()
        self.morphemes = set()

    def read(self, file):
        translator = self.read2()
        translator.__next__()

        with open(file, 'rt') as f:
            for line in f:
                pre_o = line.strip('pre: ').split()
                in_o = next(f).strip('in: ').split()
                translator.send((pre_o, in_o))

        translator.close()

    def read2(self):
        maker = Solution()
        while True:
            pre_o, in_o = (yield)
            root = maker.buildTree(pre_o, in_o)
            tree = TaskTree(root)
            self.add(tree)

    def add(self, tree):
        self.dict[tree.head.value] = tree

    def write(self, filename):
        with open(filename, 'xt') as f:
            for tree in self.dict.values():
                print(f"pre: {' '.join(tree.preorder())}", file=f)
                print(f"in: {' '.join(tree.inorder())}", file=f)

    def printall(self):
        for key,val in self.dict.items():
            print(f'{key}:  {val}')

    # ---- future ---- #
    def search(self, raw_term):
        matches = []
        # term = morphemes(raw_term)
        for tree in self.dict.values():
            # match = intersection(tree.morphemes, term)
            # if len(match) > 0:
            #    matches.append((tree, len(match)))
            ...


if __name__ == '__main__':
    a = TreeIO()
    a.read('test.txt')
    a.printall()
    a.write('test2.txt')

