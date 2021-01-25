import unittest
import random
import scorer


class Individual:
    def __init__(self, gene):
        # self.teams = teams[0]
        # self.pizzas = pizzas
        self.gene = gene
        self.fitness = None

    def get_score(self, teams, pizzas):
        deliveries = []
        sorted_pizzas = list(self.gene.items())
        sorted_pizzas.sort(key=lambda x: x[1])
        sorted_pizzas = list(map(lambda view: pizzas[view[0]], sorted_pizzas))

        current_index = 0
        for team in teams:
            deliveries.append(sorted_pizzas[current_index:team])
            current_index += team

        self.fitness = scorer.get_score(deliveries)
        return self.fitness

    @staticmethod
    def random_individual(problem):
        def get_randomised_list(items):
            indices = list(range(len(items)))
            gene = {}
            result = []

            for _ in range(len(items)):
                random_index = random.randint(0, len(indices) - 1)
                # map the original item index to it's new index
                gene[indices[random_index]] = len(result)
                result.append(items[indices[random_index]])
                del indices[random_index]

            return result, gene

        _, gene = get_randomised_list(problem.pizzas)

        return Individual(gene)

    @staticmethod
    def crossover(parent1, parent2):
        child_gene = {}

        for i in range(len(parent1.gene.keys())):
            if (i % 2 == 0):
                parent = parent1
            else:
                parent = parent2

            index = parent.gene[i]
            child_gene[i] = index

        child = Individual(child_gene)
        return child

    @staticmethod
    def mutate(individual):
        gene = individual.gene
        max_index = max(len(gene.keys()) - 1, 0)

        for _ in range(random.randint(1, max_index)):
            random_index_1 = random.randint(0, max_index)
            random_index_2 = random.randint(0, max_index)

            random_loc_1 = gene[random_index_1]
            random_loc_2 = gene[random_index_2]

            individual.gene[random_index_2] = random_loc_1
            individual.gene[random_index_1] = random_loc_2


class TestIndividual(unittest.TestCase):

    def test_crossover(self):
        parent1 = Individual(
            {0: 0, 1: 1}
        )
        parent2 = Individual(
            {0: 1, 1: 0}
        )
        child = Individual.crossover(parent1, parent2)

        self.assertEqual(child.gene, {0: 0, 1: 0})


if __name__ == '__main__':
    unittest.main()
