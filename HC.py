import numpy as np


class HC:
    def __init__(self, cand_sol, cost_matrix):
        self.c = cand_sol
        self.cm = cost_matrix

    def __call__(self):
        _iter = 0
        while _iter < 30:
            neighbs = self.generate_neighbs()
            v = self.best_neighb(neighbs)
            if self.evaluate_cost(v) < self.evaluate_cost(self.c):
                self.c = np.copy(v)
            else:
                return self.c
            _iter += 1

    def best_neighb(self, neighbs):
        costs = []
        for n in neighbs:
            costs.append(self.evaluate_cost(n))
        costs = np.array(costs)
        return neighbs[np.argmin(costs)]

    def evaluate_cost(self, sol):
        cost = 0
        for i in range(len(sol)):
            if i == len(sol)-1:
                cost += self.cm[sol[i], 0]
            else:
                cost += self.cm[sol[i], sol[i+1]]
        return cost

    def generate_neighbs(self):
        neighbs = []
        for i in range(1, len(self.c)-1, 1):
            for j in range(i+1, len(self.c), 1):
                temp = np.copy(self.c)
                temp[i], temp[j] = temp[j], temp[i]
                neighbs.append(temp)
        neighbs = np.array(neighbs)
        return neighbs


def main():
    cand_sol = np.loadtxt('candidate_sol.in', dtype=np.int8)
    cost_matrix = np.loadtxt('cost_matrix.in', dtype=np.int8)
    hc = HC(cand_sol, cost_matrix)
    out = hc()
    print('Solution: ', out)
    print('Cost: ', hc.evaluate_cost(out))


if __name__ == '__main__':
    main()
