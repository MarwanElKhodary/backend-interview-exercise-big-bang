# Automata Backend Exercise

This is a modern take on the classic "Rock, Paper, Scissors" game, with two additional choices: Lizard and Spock. The extended rules create more possible outcomes, adding depth and strategy to the game.

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MarwanElKhodary/backend-interview-exercise-big-bang.git
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:

     ```Powershell
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the dependencies from requirements.txt:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

To start the game, run:

```bash
python3 src/main.py
```

### Game Commands

Once the game is running, you can use the following commands:

- `start` - Begin playing the game
- `score` - Display the current scores
- `rules` - Show all game rules
- `reset` - Reset the scoreboard
- `quit` - Exit the game
- `help` - Show available commands

## Running Tests

This project uses pytest for testing. To run all tests:

```bash
pytest
```
