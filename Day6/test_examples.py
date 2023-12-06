from part1 import *

class TestClass:
    def test_part1_example1(self):
        assert get_ways_to_win(7, 9) == 4

    def test_part1_example2(self):
        assert get_ways_to_win(15, 40) == 8

    def test_part1_example3(self):
        assert get_ways_to_win(30, 200) == 9