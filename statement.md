# Project Statement: Command-Line Tic Tac Toe in Python

## 1. Problem Statement
Traditional pencil-and-paper games like Tic Tac Toe are often inaccessible or impractical when physical media is unavailable. Existing digital alternatives frequently rely on complex Graphical User Interfaces (GUIs) or external dependencies, making them overly resource-intensive or difficult to run in minimal developer environments. 

There is a need for a lightweight, dependency-free, terminal-based implementation of Tic Tac Toe that allows two players to play locally on any system with a Python 3 runtime.

---

## 2. Scope of the Project
The project covers the development of a standard, two-player console application written in pure Python.

### Included in Scope
* **Game Logic:** Turn-based gameplay enforcing standard 3x3 grid mechanics.
* **Dynamic Board Display:** Real-time text rendering of grid positions (0–8) and occupied spaces (`X` and `O`).
* **Win Condition Evaluation:** Automated checking across all 8 possible winning combinations (rows, columns, diagonals).
* **Game Loop Management:** Infinite loop handling turn switches until a game-ending condition occurs.

### Out of Scope
* Graphical user interfaces (GUI) or web implementations.
* Single-player artificial intelligence (AI) opponents.
* Move validation (e.g., handling invalid index inputs or overwriting already occupied positions).
* Tie/Draw detection handling when the grid fills without a winner.
* Score tracking across multiple rounds or online multiplayer support.

---

## 3. Target Users
* **Beginner Python Developers:** Programmers looking for straightforward reference code to understand list state management, conditional loops, and modular function structures in Python.
* **Terminal Enthusiasts & Students:** Users looking for a quick, zero-dependency console game for local two-player recreation directly from the command line.

---

## 4. High-Level Features

### 1. Dynamic Console Rendering
* Renders a 3x3 matrix showing numerical indices (0–8) for unplayed positions and visual markers (`X` or `O`) for played spots.

### 2. State-Based Turn Management
* Maintains separate bitmask lists (`xState` and `zState`) to track player selections and automatically toggles turns between Player X and Player O.

### 3. Automated Win Detection
* Evaluates board states against horizontal, vertical, and diagonal winning sets after every turn using custom aggregation logic (`sum()`).

### 4. Interactive Input Prompt
* Simple numerical input interface mapping user selections directly to the board array index.