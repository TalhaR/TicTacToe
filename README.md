# Tic-Tac-Toe
Classic Tic-Tac-Toe Game with GUI

# Requirements
- Python3.x or higher

# Instructions
1. Clone or download the repository.
2. On MacOS, just double-click the TTT application.

# Controls
- Click on a tile to place 'X' or 'O'. Game will alternate between by default.
- At any point press 'r' to start a new game

# Miscellaneous 
I used this command to convert my python files into an executable. Requires PyInstaller.
>pyinstaller --noconfirm --onefile --noconsole --icon "/Users/talha/PycharmProjects/TicTacToe/assets/icon.ico" --name "TTT" --add-data "/Users/talha/PycharmProjects/TicTacToe/assets:assets/"  "/Users/talha/PycharmProjects/TicTacToe/game.py"