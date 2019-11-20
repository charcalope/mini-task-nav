from query import query
from TreeNode import TreeNode

class TaskTree:
    def __init__(self, outcome=None):
        if outcome is None:
            self.intro()
            gen = self.build_from(self.head)
            try:
                gen.__next__()
            except StopIteration:
                print('Exiting ... ')
                print()

        else:
            self.head = TreeNode(value=outcome)

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

    def print(self):
        def _iter_(node):
            if node is None:
                return
            else:
                yield from _iter_(node.down)
                yield node.value
                yield from _iter_(node.right)

        for val in _iter_(self.head):
            print(val)


if __name__ == '__main__':
    a = TaskTree()
    a.print()
