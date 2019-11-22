from query import query
from TreeNode import TreeNode
from Solution import Solution

class TaskTree:
    def __init__(self, outcome=None):
        self.morphemes = set()
        if outcome is None:
            self.intro()
            gen = self.build_from(self.head)
            try:
                gen.__next__()
            except StopIteration:
                print('Exiting ... ')
                print()
        else:
            self.head = outcome

    def intro(self):
        print("Let's create a new interaction.")
        outcome = input('The desired outcome is that a person ...')
        print()
        self.head = TreeNode(value=outcome)
        print("Great. Now let's decompose our desired outcome.")
        print()
        print('After the prompt, enter a few steps.')
        print('Remember, these steps can be clarified and edited later.')
        print()

    def build_from(self, node):
        """ Builds out a path based on user input. """
        # TODO: describe generator better

        try:
            while True:
                direct = query(node)
                print()
                print(direct)

                # return -> navigate up
                if direct is '  ':
                    yield
                # clarify -> navigate down
                elif direct is '':
                    yield from self.build_from(node.down)
                # continue -> navigate right
                elif direct is ' ':
                    yield from self.build_from(node.right)
                # quit
                else:
                    raise StopIteration
        # TODO: handle quitting so that user doesn't have to manually go up
        except StopIteration:
            return

    def preorder(self):
        def _iter_(node):
            if node is None:
                return
            else:
                yield node.value
                yield from _iter_(node.down)
                yield from _iter_(node.right)

        yield from _iter_(self.head)

    def inorder(self):
        def _iter_(node):
            if node is None:
                return
            else:
                yield from _iter_(node.down)
                yield node.value
                yield from _iter_(node.right)

        yield from _iter_(self.head)

    def print(self):
        print(f'Preorder: {[a for a in self.preorder()]}')
        print(f'Inorder: {[a for a in self.inorder()]}')

    # ---- future ---- #
    def index_from(self, TreeIO):
        candidates = [a for a in self.inorder()]
        candidates = set(candidates)
        new = [candidates in TreeIO.morphemes]
        self.morphemes.add(new)


if __name__ == '__main__':
    #a = TaskTree()
    pre_o = ['id', 'doc', 'pid', 'bc', 'ssn', 'pr', 'dmv']
    in_o = ['bc', 'ssn', 'pid', 'pr', 'doc', 'dmv', 'id']

    test = Solution()
    res = test.buildTree(pre_o, in_o)

    t_tree = TaskTree(res)
    t_tree.print()

