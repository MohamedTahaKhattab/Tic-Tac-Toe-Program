# Tic-Tac-Toe Multiplayer Game

A networked multiplayer Tic-Tac-Toe game built with Python using Tkinter for the GUI and socket programming for client-server communication.

## Features

- **Multiplayer Support**: Two players can play against each other over a network
- **Real-time Gameplay**: Moves are synchronized between players instantly
- **Graphical Interface**: Clean and simple GUI using Tkinter
- **Automatic Win Detection**: Game automatically detects wins, losses, and draws
- **Game Reset**: Automatic board reset after each game ends

## Architecture

The game follows a client-server architecture:

- **Server** (`X_O_Server.py`): Handles communication between two clients
- **Player 1** (`X_O_Player1.py`): Plays as 'X' and goes first
- **Player 2** (`X_O_Player2.py`): Plays as 'O' and goes second

## Requirements

- Python 3.x
- tkinter (usually comes with Python)
- socket (built-in Python module)
- _thread (built-in Python module)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd Tic-Tac-Toe-Program
```

2. Ensure you have Python 3.x installed on your system

## How to Run

### Step 1: Start the Server
```bash
python X_O_Server.py
```
The server will start listening on `127.0.0.1:7772` and wait for two clients to connect.

### Step 2: Start Player 1 (X)
```bash
python X_O_Player1.py
```
This will open a window for Player 1 who plays as 'X' and gets the first turn.

### Step 3: Start Player 2 (O)
```bash
python X_O_Player2.py
```
This will open a window for Player 2 who plays as 'O' and goes second.

## Gameplay

1. **Player 1 (X)** starts first
2. Click on any empty cell to place your symbol
3. The move is automatically sent to the opponent
4. Players take turns until someone wins or the board is full
5. The game automatically resets after each round

## Game Rules

- Standard Tic-Tac-Toe rules apply
- 3x3 grid
- First player to get 3 in a row (horizontally, vertically, or diagonally) wins
- If all 9 spaces are filled without a winner, it's a draw

## Network Configuration

By default, the game runs on:
- **Host**: `127.0.0.1` (localhost)
- **Port**: `7772`

To change the network settings, modify the connection parameters in all three files:
```python
# In X_O_Server.py
server = TicTacToeServer("your_host", your_port)

# In X_O_Player1.py and X_O_Player2.py
client = TicTacToeClient("your_host", your_port)
```

## File Structure

```
Tic-Tac-Toe-Program/
├── README.md
├── X_O_Server.py      # Server handling client connections
├── X_O_Player1.py     # Player 1 client (X)
└── X_O_Player2.py     # Player 2 client (O)
```

## Technical Details

- **GUI Framework**: Tkinter
- **Networking**: TCP sockets
- **Threading**: Multi-threading for handling simultaneous client connections
- **Communication Protocol**: Simple text-based protocol sending button positions

## Troubleshooting

### Common Issues

1. **Connection Refused**: Make sure the server is running before starting the clients
2. **Port Already in Use**: Close any existing instances or change the port number
3. **GUI Not Responding**: Ensure tkinter is properly installed with your Python distribution

### Error Messages

- If you see "connection refused", start the server first
- If the game freezes, restart all components (server and both clients)

## Future Enhancements

Potential improvements for this project:
- Add spectator mode
- Implement player names/usernames
- Add game statistics tracking
- Support for multiple simultaneous games
- Enhanced GUI with themes
- Network play over the internet (not just localhost)

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## Author
Mohamed Taha Khattab - mohamed.taha.khattab0@gmail.com
