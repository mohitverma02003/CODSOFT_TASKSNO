# CODSOFT Task 2 — Tic-Tac-Toe AI

## Overview
This project is an interactive Tic-Tac-Toe game where a human player competes against an unbeatable Artificial Intelligence. It was developed as Task 2 for the CODSOFT Artificial Intelligence Internship. 

## Objective
To implement an AI agent capable of playing Tic-Tac-Toe optimally against a human player using game theory and search algorithms.

## Features
- **Unbeatable AI:** The AI uses the Minimax algorithm, ensuring it will never lose. It forces a draw at worst, and wins if the human makes a mistake.
- **Interactive UI:** A clean, web-based graphical interface built with Streamlit.
- **Real-time Gameplay:** The AI calculates its moves instantly and the board updates automatically.

## Technologies Used
- Python 3
- Streamlit (for User Interface)
- Math module (for infinity values)

## How the AI Works (Minimax & Alpha-Beta Pruning)
The AI is powered by the **Minimax Algorithm**, a recursive decision-making algorithm used in zero-sum games. 
- The AI evaluates all possible future moves and board states to find the optimal move.
- The AI plays as the **Maximizer**, aiming for the highest score (+10).
- The human is modeled as the **Minimizer**, aiming for the lowest score (-10).
- To optimize performance, the AI uses **Alpha-Beta Pruning**. This technique stops evaluating branches of the game tree that are guaranteed to be worse than previously examined branches, drastically reducing computation time without affecting the AI's unbeatable nature.

## Installation & Running the Game

1. Ensure Python is installed on your system.
2. Clone this repository.
3. Navigate to the project directory:
   ```bash
   cd Task2_Tic_Tac_Toe_AI
