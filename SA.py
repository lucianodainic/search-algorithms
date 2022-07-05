import numpy as np


class SA:
    def __init__(self, cand_sol, cost_matrix):
        self.c = cand_sol
        self.cm = cost_matrix

    def __call__(self):
        _iter = 30
        T = 100
        while T > 0:
            while _iter > 0:
                neighbs = self.generate_neighbs()
                v = neighbs[np.random.randint(0, len(neighbs))]
                if self.evaluate_cost(v) < self.evaluate_cost(self.c):
                    self.c = np.copy(v)
                else:
                    if np.random.rand() < self.p(v, T):
                        self.c = np.copy(v)
                _iter -= 1
            T -= 0.1
        return self.c

    def p(self, v, T):
        if self.evaluate_cost(v) < self.evaluate_cost(self.c):
            return 1
        elif self.evaluate_cost(v) >= self.evaluate_cost(self.c):
            return np.e ** (-(self.evaluate_cost(v) - self.evaluate_cost(self.c))/T)

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
    sa = SA(cand_sol, cost_matrix)
    out = sa()
    print('Solution: ', out)
    print('Cost: ', sa.evaluate_cost(out))


if __name__ == '__main__':
    main()
