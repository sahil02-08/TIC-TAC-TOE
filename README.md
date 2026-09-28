# Command Line Tic-Tac-Toe Game

A lightweight, terminal-based Tic-Tac-Toe game written in pure Python. This project allows two players to play locally using numerical positional inputs on a dynamic $3 \times 3$ grid.

---

## Overview

This application brings the classic game of Tic-Tac-Toe into a clean, text-based interactive interface. It tracks player turns, updates the board visually after each move, checks all possible winning combinations dynamically, and announces the winner upon match completion.

It is ideal as a simple Python demonstration project or a lightweight mini-game for terminal environments.

---

## Features

- **Interactive Dynamic Board**: Visualizes the $3 \times 3$ grid and automatically labels empty positions with numbers `0-8` for easy user input.
- **Turn-Based Gameplay**: Manages smooth alternating turns between **Player X** and **Player O**.
- **Instant Win Detection**: Evaluates rows, columns, and diagonals after every turn to detect wins instantly.
- **Zero External Dependencies**: Built entirely with Python standard libraries, requiring no extra package installations.

---

## Technologies & Tools Used

- **Language**: Python 3.x
- **Development Tools**: Any standard IDE or terminal environment (VS Code, PyCharm, Terminal/Command Prompt).

---

## Steps to Install & Run

### Prerequisites
Make sure you have **Python 3** installed on your system. You can verify this by running:
```bash
python --version
```
or
```bash
python3 --version
```

### Installation

1. **Clone or Download** this repository or copy the code into a file named `main.py`.
   ```bash
   git clone https://github.com/your-username/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. **Run the Game**  
   Execute the script directly using Python:
   ```bash
   python main.py
   ```
   *(Use `python3 main.py` depending on your operating system configuration).*

---

## How to Play

1. When the game starts, you will see a numbered grid ($0$ through $8$):

```text
0 | 1 | 2
---|---|---
3 | 4 | 5
---|---|---
6 | 7 | 8
```

2. **Player X** goes first. Enter a number between `0` and `8` corresponding to the cell where you want to place your mark.
3. **Player O** takes the next turn.
4. The first player to align 3 marks horizontally, vertically, or diagonally wins the match!

---

## Testing Instructions

To ensure the game functions properly, you can perform manual testing using the following test scenarios:

### Test Case 1: Horizontal Win (Player X)
1. Run the game.
2. Enter the following inputs sequentially when prompted:
   - Player X: `0`
   - Player O: `3`
   - Player X: `1`
   - Player O: `4`
   - Player X: `2`
3. **Expected Result**: Output prints `"X Won the match"` and `"Match over"`, then terminates successfully.

### Test Case 2: Diagonal Win (Player O)
1. Run the game.
2. Enter inputs to let Player O take a diagonal path ($0, 4, 8$):
   - Player X: `1`
   - Player O: `0`
   - Player X: `2`
   - Player O: `4`
   - Player X: `5`
   - Player O: `8`
3. **Expected Result**: Output prints `"O Won the match"` and `"Match over"`, then terminates successfully.

---

## Screenshots & Demo

### Initial Game State
```text
Welcome to Tic Tac Toe
0 | 1 | 2 
---|---|---
3 | 4 | 5 
---|---|---
6 | 7 | 8 
X's Chance
Please enter a value: 4
```

### Gameplay In Progress
```text
0 | 1 | 2 
---|---|---
3 | X | 5 
---|---|---
6 | 7 | 8 
O's Chance
Please enter a value: 0
```

### Winning State Example
```text
O | 1 | 2 
---|---|---
3 | X | 5 
---|---|---
6 | 7 | 8 
X Won the match
Match over
```

---

## License

This project is open-source and free to use or modify for learning and educational purposes.
