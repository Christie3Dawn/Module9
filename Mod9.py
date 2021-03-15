import copy
import itertools
import unittest


class CopyTest(unittest.TestCase):
    def test_is_id_equal(self):
        # using alias
        animals = ['lion', 'bear', 'tiger']
        animals2 = animals
        animals3 = animals2
        self.assertEqual(id(animals), id(animals2))
        self.assertEqual(id(animals), id(animals3))
        self.assertEqual(len(animals), len(animals2))
        self.assertEqual(animals[2], animals2[2])

    def test_append_hijinx(self):
        animals = ['lion', 'bear', 'tiger']
        animals2 = animals
        animals3 = animals2

        animals2 = ['dog', 'cat', 'bird']
        animals3.append('cougar')

        # make sure that animals and animals3 stay the same
        self.assertEqual(id(animals), id(animals3))

        # make sure that asnimals2 is a new list
        self.assertNotEqual(id(animals), id(animals2))

        # make sure that append happened to animals an animals3
        self.assertEqual(animals[3], animals3[3])

    def test_deep_copy(self):
        animals = ['lion', 'bear', 'tiger']
        animals2 = animals.copy()
        animals3 = animals2.copy()
        self.assertNotEqual(id(animals), id(animals2))
        self.assertNotEqual(id(animals), id(animals3))
        self.assertNotEqual(id(animals2), id(animals3))
        animals.append("cougar")
        self.assertNotEqual(len(animals), len(animals3))
        self.assertNotEqual(len(animals), len(animals2))


class IterTest(unittest.TestCase):
    def test_cycle_break(self):
        a = [1, 2, 3, 4, 5]
        # If I want it to stop
        counter = 0
        for i in itertools.cycle(a):
            print(i)
            counter = counter + 1
            if counter > 19:
                break
        self.assertEqual(counter, 20)

    def test_count(self):
        x = []
        for i in itertools.count(start=1, step=10):
            if i > 110:
                break
            else:  # Don't need else statement. Can just use print statement
                x.append(i)
        self.assertEqual(len(x), 11)
        self.assertEqual(x[2], 21)

    def test_repeat(self):
        x = []
        for i in itertools.repeat("Team", 5):
            x.append(i)
        self.assertEqual(len(x), 5)
        self.assertEqual(x[2], "Team")


if __name__ == '__main__':
    unittest.main()
