# CUDA-Accelerated Reinforcement Learning for Route Optimization

This project leverages reinforcement learning (RL) to tackle complex route optimization challenges in logistics, transportation, and navigation systems. By designing a custom OpenAI Gym environment and training an RL agent using methods such as PPO or DQN with CUDA-accelerated PyTorch—we aim to develop efficient, adaptive routing strategies.

## Overview

- **Objective:**  
  Learn optimal routing strategies in dynamic, grid-based environments while minimizing computational costs.

- **Approach:**  
  - **Environment:**  
    A custom Gym environment simulates various route optimization scenarios, including obstacles and dynamic traffic conditions.
  - **RL Model:**  
    The agent is trained using algorithms like PPO or DQN (via Stable-Baselines3) to navigate the environment and optimize routes.
  - **Acceleration:**  
    A performance comparison is made between CPU and CUDA-powered GPU implementations to assess training efficiency and model accuracy.
  - **Demo:**  
    A simplified 5x5 maze example introduces the fundamentals of the Markov Decision Process and demonstrates core RL concepts.

## Getting Started

1. **Install Dependencies:**  
   Ensure Python is installed and run:
   ```bash
   pip install gym==0.23.0 stable-baselines3 torch
2. Run the Notebook:
Open the provided Colab notebook to explore the introductory 5x5 maze example and the broader RL model implementation.

3. Experiment:
Modify the Gym environment and RL parameters to test different routing scenarios and compare CPU vs. GPU training performance.
