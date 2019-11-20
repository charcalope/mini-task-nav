from functools import reduce
from TreeNode import TreeNode
import re

def query(node):
    """Queries user for direction, builds out path if empty,
        then returns response."""

    def nav_choice_from(node):
        """ Prompts user for desired action, then returns input string.
            If action would be navigation to empty path, prompts user for
            further input before continuing. """

        direction = instruction_response(node)

        if direction is ' ':
            if node.right is None:
                node.right = parse_step()
            return ' '

        if direction is '':
            # empty path, update in place
            if node.down is None:
                node.down = parse_step(node.value)
            return ''
        else:
            return direction

    def instruction_response(node):
        print('Current step:')
        print(f'    - {node.value}')
        return input('Press (enter) to clarify, or (spacebar) to continue.'
                     'To return to previous step, double tap (spacebar).')

    def parse_step(outcome=None):
        def parser(s):
            """ Returns string as a list of steps."""
            p = re.compile(r'\band\b|\bthen\b|,[\s]*')
            return p.split(s)

        def linkright(values):
            """ Returns a right linked list from a list of values. """

            def link_before(node, other):
                other.right = node
                return other

            # note: list.reverse() reverses in place, so returns None
            # use reversed(list) for iterator
            def as_node(values):
                return map(lambda x: TreeNode(x), reversed(values))

            return reduce(link_before, as_node(values))

        if outcome is not None:
            raw_input = input(f'in order to {outcome}...')
        else:
            raw_input = input('next step... ')

        return linkright(parser(raw_input))

    return nav_choice_from(node)