# TODO: Implement a stack data structure using an array

import pytest

class Stack():
    def __init__(self):
        self.isEmpty = True
    def is_empty(self):
        return self.isEmpty

    def push(self, element):
        self.isEmpty = False
        return self.isEmpty

class TestStack():
    def setup_method(self):
        self.stack = Stack()
    def test_new_stack_is_empty(self):
        assert self.stack.is_empty()

    def test_push(self):
        self.stack.push(0)
        assert not self.stack.is_empty()












