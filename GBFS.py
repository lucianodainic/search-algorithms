from Node import Node
import ast
import numpy as np
from numpy import linalg as la
import time
import os
import psutil

class GBFS:
    def __init__(self, Q, goal_state):
        self.frontier = Q
        self.goal_state = goal_state
        self.reached = []
        
    def __call__(self, init_state):
        fin_state = False
        nr_visit = 0
        self.reached.append(init_state)
        while self.frontier and not fin_state:
            self.sort_Q()
            node = self.frontier.pop(0)
            nr_visit += 1
            if not self.is_goal_state(node):
                self.generate_states(node)
            else:
                fin_state = True
        return node, nr_visit

    def is_goal_state(self, node):
        if ((np.array(node.state) == self.goal_state).all()):
            return True
        else:
            return False

    def generate_states(self, node):
        for m in range(len(node.state)):
            for n in range(len(node.state)):
                if node.state[m][n] == 0:
                    i, j = m, n
                    break
        if i-1 < 3:
            A = np.array(node.state)
            A[i,j], A[i-1,j] = A[i-1,j], A[i,j]
            if not self.already_created(A):
                self.reached.append(A)
                new_node = Node(A, node, la.norm(A-self.goal_state,1))
                node.insert(new_node)
                self.frontier.append(new_node)
        if j+1 < 3:
            A = np.array(node.state)
            A[i,j], A[i,j+1] = A[i,j+1], A[i,j]
            if not self.already_created(A):
                self.reached.append(A)
                new_node = Node(A, node, la.norm(A-self.goal_state,1))
                node.insert(new_node)
                self.frontier.append(new_node)
        if j-1 < 3:
            A = np.array(node.state)
            A[i,j], A[i,j-1] = A[i,j-1], A[i,j]
            if not self.already_created(A):
                self.reached.append(A)
                new_node = Node(A, node, la.norm(A-self.goal_state,1))
                node.insert(new_node)
                self.frontier.append(new_node)
        if i+1 < 3:
            A = np.array(node.state)
            A[i,j], A[i+1,j] = A[i+1,j], A[i,j]
            if not self.already_created(A):
                self.reached.append(A)
                new_node = Node(A, node, la.norm(A-self.goal_state,1))
                node.insert(new_node)
                self.frontier.append(new_node)
        return None
    def already_created(self, new_state):
        bool = []
        for elem in self.reached:
            if ((new_state == np.array(elem)).all()):
                bool.append(True)
            else:
                bool.append(False)
        if True in bool:
            return True
        else:
            return False
    def sort_Q(self):
        for j in range(1,len(self.frontier)):
            key = self.frontier[j]
            i=j-1
            while i>0 and self.frontier[i].manh>key.manh:
                self.frontier[i+1] = self.frontier[i]
                i=i-1
            self.frontier[i+1]=key 

def main():
    f = open('states.in','r')
    init_state = np.array(ast.literal_eval(f.readline()))
    goal_state = np.array(ast.literal_eval(f.readline()))
    f.close()
    init_state_node = Node(init_state,None,la.norm(init_state-goal_state,1))
    queue = []
    queue.append(init_state_node)
    tic = time.time()
    gbfs = GBFS(queue, goal_state)
    res,n = gbfs(init_state)
    tac = time.time()
    print('Algorithm Time: ', tac-tic)
    print('No. of visited Nodes: ',n)
    process = psutil.Process(os.getpid())
    print('Used Memory (bytes): ',process.memory_info().rss) 
    print('Heuristic Function: Manhattan Norm')
    print('Path: ')
    res.print_tree_by_parent()

if __name__ == '__main__':
    main()