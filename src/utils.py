import os

def clear_screen() -> None:
    """
    Clear the console screen - works on Windows and macOS
    """
    os.system('cls' if os.name == 'nt' else 'clear')