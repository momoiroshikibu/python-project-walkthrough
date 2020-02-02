import unittest
from walkthrough.bird import Bird

class SayHelloTest(unittest.TestCase):

    def test_1(self):
        bird = Bird('pink')
        actual = bird.fly()
        expect = 'flying: pink'
        assert(actual == expect)
