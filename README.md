# 🎯 Darts Scoreboard (Python)

A simple Python project simulating a **501 darts game** for two players.  
It tracks scores, averages, and determines the winner, with added features like:
- Input validation using `try/except` to prevent invalid scores.
- Automatic CSV export of game results (`darts_results.csv`).
- Basic **data visualisation** with `matplotlib` to show score progression.

## Example Features
- Alternate turns between players.
- Prevents invalid scores (e.g., <0 or >180).
- Overshoot handling (keeps previous score if you go below 0).
- Saves results and averages for each match.
- Plots a graph of per-turn scoring.

## Future Plans
- Extend to track **running averages** on the graph.
- Display results on a **TFT screen via ESP32**.
- Possible GUI version (Tkinter or PyQt).

## How to Run
: Jupyter Notebook
1. Open the notebook in Jupyter:
   ```bash
   jupyter notebook Dartsscoreboard.ipynb

