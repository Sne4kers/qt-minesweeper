# Qt-minesweeper
My first pyQt application. Mainly serves as a sandbox and a first try of pyQt.

## Setup

You should have PyQt6 installed. Simply run this command to download all required files
```
pip install PyQt6
```

## Gameplay

You can play a regular minesweeper game. At the top of the game screen you can see counter of bombs left calculated based on amount of marked cells. You can mark cells as bombs by pressing right mouse button.
It is impossible to lose a game with a first click. You can restart a game by pressing button with a smile at the top of fthe screen.
If you press on the bomb button, buttons will be disabled and bombs will be shown. Also, button with a face will turn into sad face. In order to win the game, you need to open all non-bomb cells and mark all bomb cells. In case of the win, face will become happy. 

You can change size of the grid and amount of bombs in the settings. They all have limitations, just so you wont make game unplayable and grid wont be outside of you screen.


Good luck on the minefield! ;)
