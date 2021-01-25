def get_score(deliveries):
    sum = 0

    for delivery in deliveries:
        ingredients = set()
        for pizza in delivery:
            for ingredient in pizza:
                ingredients.add(ingredient)
        sum += (len(ingredients) ** 2)

    return sum


import unittest

class TestScorer(unittest.TestCase):

    def test_score(self):
        deliveries = [
            [
                ['a', 'b'],
                ['c', 'd']
            ],
            [
                ['a', 'b'],
                ['a', 'c']
            ]
        ]
        self.assertEqual(get_score(deliveries), 25)


if __name__ == '__main__':
    unittest.main()
