import random
from itertools import permutations
from typing import List
import numpy as np

def compute_mdp(sbox: List[int]) -> float:
    n = len(sbox)
    ddt = np.zeros((n, n), dtype=int)
    for dx in range(n):
        for x in range(n):
            x_prime = x ^ dx
            dy = sbox[x] ^ sbox[x_prime]
            ddt[dx][dy] += 1
    return ddt[1:].max() / n  

POP_SIZE = 100
MAX_GENERATIONS = 1000
MUTATION_RATE = 0.2
TOURNAMENT_SIZE = 5
TARGET_MDP = 0.25

def initialize_population():
    base = list(range(16))
    return [random.sample(base, 16) for _ in range(POP_SIZE)]

def select(population, fitnesses):
    selected = random.sample(list(zip(population, fitnesses)), TOURNAMENT_SIZE)
    selected.sort(key=lambda x: x[1]) 
    return selected[0][0]

def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [-1] * size
    child[start:end] = parent1[start:end]
    ptr = 0
    for gene in parent2:
        if gene not in child:
            while child[ptr] != -1:
                ptr += 1
            child[ptr] = gene
    return child

def mutate(sbox):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(16), 2)
        sbox[i], sbox[j] = sbox[j], sbox[i]
    return sbox

population = initialize_population()
best_sbox = None
best_mdp = 1.0

for generation in range(MAX_GENERATIONS):
    fitnesses = [compute_mdp(sbox) for sbox in population]
    for sbox, mdp in zip(population, fitnesses):
        if mdp <= TARGET_MDP:
            best_sbox = sbox
            best_mdp = mdp
            break
    if best_sbox:
        break
    new_population = []
    for _ in range(POP_SIZE):
        parent1 = select(population, fitnesses)
        parent2 = select(population, fitnesses)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
    population = new_population

print("Best S-box:", best_sbox)
print("Best MDP:", best_mdp)
