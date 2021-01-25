import random
from ga.components import Individual

class GASolver:
    def __init__(self, problem):
        self.population_size = 100
        self.num_generations = 100
        self.elitsm = 0.1
        self.mutation_probability = 0.5
        self.log_interval = 10
        self.problem = problem
        self.flattened_teams = []
        for key in problem.teams.keys():
            for _ in range(problem.teams[key]):
                self.flattened_teams.append(key)

    def get_initial_population(self, problem):
        population = []
        for _ in range(self.population_size):
            population.append(Individual.random_individual(problem))
        
        return self.sort_population(population)

    def sort_population(self, population):
        def sortByFitness(element):
            return element.get_score(
                self.flattened_teams, self.problem.pizzas)

        population.sort(reverse=True, key=sortByFitness)
        return population

    def select(self, population):
        random_index = random.randint(0, len(population) - 1)
        return population[random_index]

    def get_next_generation(self, current_population):
        num_elites = int(self.elitsm * self.population_size)
        new_population = current_population[:num_elites]

        for _ in range(self.population_size - num_elites):
            parent1 = self.select(current_population)
            parent2 = self.select(current_population)
            child = Individual.crossover(parent1, parent2)

            if (random.random() <= self.mutation_probability):
                Individual.mutate(child)

            new_population.append(child)

        return self.sort_population(new_population)

    def run(self):
        population = self.get_initial_population(self.problem)

        for i in range(1, self.num_generations):
            if (i % self.log_interval == 0):
                print("Generation {0}: fittest: {1}".format(i, population[0].fitness))
            population = self.get_next_generation(population)

        print("Fittest: {}".format(population[0].fitness))
