# CUDA-Accelerated Reinforcement Learning for Route Optimization

This project explores reinforcement learning (RL) as a method for solving route optimization tasks within a 5x5 maze environment. It compares RL-based solutions with traditional algorithms such as Dijkstra's and A* and includes CUDA acceleration for potential speed-up.

## Overview

- **Objective:**  
  Learn adaptive, efficient routing strategies in a grid-based environment using reinforcement learning.

- **Approach:**  
  - **Environment:**  
    A custom 5x5 maze implemented using a Gym-style environment.
  - **Traditional Algorithms:**  
    Implementations of Dijkstra’s, A*, and DFS for pathfinding benchmark comparisons.
  - **RL Techniques:**  
    Reinforcement learning models built using value iteration, on-policy, and off-policy Monte Carlo methods.
  - **CUDA Acceleration:**  
    Simple CUDA-based parallelized example included to demonstrate GPU benefits in RL workflows.

## Traditional Methods

The following classical pathfinding algorithms are implemented in the `Traditional Methods/` directory:
- `A*_solver.py`
- `Dijkstra_solver.py`
- `DFS_solver.py`

These scripts find the optimal path from the start to the goal in a 5x5 maze and are used to benchmark RL agents.

## Getting Started

1. **Install Dependencies:**

    ```bash
    pip install gym==0.23.0 pygame stable-baselines3 torch
    ```

2. **Run the Notebook or Python Scripts:**
   - Try out the `MDP_introduction.ipynb` notebook for an introduction to value iteration and policy evaluation.
   - Explore `on_policy_control_complete.py` and `off_policy_control_complete.py` to see RL agents in action.

3. **Experiment:**
   - Modify the maze or agent behavior.
   - Compare results across RL and traditional algorithms.
   - Experiment with CUDA acceleration using `CUDA_acceleration.py`.
