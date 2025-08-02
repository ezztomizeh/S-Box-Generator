# 🔐 Genetic Algorithm for Designing S-boxes with Low MDP

This repository contains the implementation of a **Genetic Algorithm (GA)** to evolve 4-bit cryptographic substitution boxes (S-boxes) with a **Maximum Differential Probability (MDP) ≤ 0.25** — a desirable property for resistance against **differential cryptanalysis**. The code is part of a larger research effort on enhancing lightweight cryptographic primitives for IoT and embedded systems, and will be presented at an upcoming cryptography/security conference.

## 🧠 Background

S-boxes are nonlinear components used in symmetric key algorithms (e.g., AES, SIMON) to introduce confusion. An S-box with low MDP is less vulnerable to differential cryptanalysis, one of the most powerful attacks against symmetric ciphers. However, designing such S-boxes with optimal cryptographic properties is computationally expensive.

This project uses a **genetic algorithm** to search the space of 4-bit permutations (16! possibilities) for candidates with MDP ≤ 0.25.

## 📜 Algorithm Description

* **Population Initialization**: Random permutations of 16 elements.
* **Fitness Evaluation**: MDP is computed using the **Difference Distribution Table (DDT)**.
* **Selection**: Tournament selection is used to choose the fittest parents.
* **Crossover**: Order-preserving crossover ensures child validity as a permutation.
* **Mutation**: With a 20% chance, two values in an S-box are swapped.
* **Termination**: Stops once an S-box with `MDP ≤ 0.25` is found or the generation limit is reached.

## 🧪 Code Overview

```python
compute_mdp(sbox: List[int]) -> float
```

Calculates the Maximum Differential Probability of an S-box by generating the DDT.

```python
initialize_population()
```

Creates the initial random population of valid 4-bit S-boxes.

```python
select(), crossover(), mutate()
```

GA operations: tournament-based selection, order-preserving crossover, and random mutation.

```python
Main Loop
```

Runs the GA for up to 1000 generations or until a satisfactory S-box is found.

## 📈 Output

The script prints:

```bash
Best S-box: [s0, s1, ..., s15]
Best MDP: 0.25
```

If no solution is found within the generation limit, the best-found S-box is returned.

## 🔬 Research Use

This implementation serves as the foundation for a proposed enhancement to the SIMON cipher using SPN-based transformation layers. The generated S-boxes are evaluated further for:

* **Avalanche Effect**
* **Nonlinearity**
* **Bit Independence**
* **Resilience against Linear/Differential attacks**

## ⚙️ Requirements

* Python 3.7+
* `numpy`

Install dependencies with:

```bash
pip install numpy
```

## 📚 Citation

The research paper will be added here once published.

## 🧑‍🔬 Author & Contact

**Ezzudin Tomizi**
For research questions, collaborations, or conference inquiries, please contact:
📧 *[ezzudintomizi@gmail.com](mailto:ezzudintomizi@gmail.com)*

---

Let me know if you want to include diagrams (e.g., DDT visualization), benchmarking data, or make this conference-paper-ready as a supplementary material package (`appendix`, `figures`, etc.).
