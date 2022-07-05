import numpy as np


class GA:
    def __init__(self, n, cost_matrix):
        self.n = n
        self.cm = cost_matrix

    def __call__(self):
        t = 0
        population = []
        costs = []

        # initialize population
        for i in range(10):
            c = np.random.permutation(self.n)
            population.append(c)
            costs.append(self.evaluate_cost(c))
        population = np.array(population)

        while t < 3:
            # selection (first 70% of most fit individuals)
            population = population[np.argsort(
                costs)[:int(0.7*len(population))]]

            population = self.recombination(population)
            population = self.mutation(population)
            costs = []
            for i in range(len(population)):
                costs.append(self.evaluate_cost(population[i]))
            t += 1
        return population[np.argmin(costs)]

    def evaluate_cost(self, sol):
        cost = 0
        for i in range(len(sol)):
            if i == len(sol)-1:
                cost += self.cm[sol[i], 0]
            else:
                cost += self.cm[sol[i], sol[i+1]]
        return cost

    def mutation(self, population):
        population = np.array(population)
        t = np.random.randint(len(population)-1)
        j = np.random.randint(self.n)
        k = np.random.randint(self.n)
        for i in range(self.n):
            if i == j:
                population[t, i] = population[t, k]
            elif i == k:
                population[t, i] = population[t, j]
            else:
                population[t, i] = population[t, i]
        return population

    def recombination(self, population):

        def common_elements(a, b):
            a_set = set(a)
            b_set = set(b)
            if len(a_set.intersection(b_set)) > 0:
                return(True)
            return(False)

        new_generation = []
        for i in range(len(population)):
            for j in range(len(population)):
                crossover_pnt = np.random.randint(low=1, high=self.n)
                if not common_elements(population[i, :crossover_pnt], population[j, crossover_pnt:]):
                    child1 = [*population[i, :crossover_pnt],
                              *population[j, crossover_pnt:]]
                    new_generation.append(child1)
                    child2 = [*population[j, crossover_pnt:],
                              *population[i, :crossover_pnt]]
                    new_generation.append(child2)
        return new_generation


def main():
    cost_matrix = np.loadtxt('cost_matrix.in', dtype=np.int8)
    n = len(cost_matrix)  # no. of cities
    ga = GA(n, cost_matrix)
    out = ga()
    print('Solution: ', out)
    print('Cost: ', ga.evaluate_cost(out))


if __name__ == '__main__':
    main()
