# Handcricket-game
Hand cricket game allows users to play a digital version of the traditional hand cricket game with the computer.
Sure, here's a detailed README content for your hand cricket game project:

---

# Hand Cricket Game in Python

## Overview

This is a simple hand cricket game implemented in Python where you play against the computer. The game involves a toss to decide who bats first, followed by two innings where you alternate between batting and bowling. The objective is to score as many runs as possible while batting and to defend your score while bowling.

## Features

- **Toss**: Decide whether to choose "ODD" or "EVEN" for the toss.
- **Batting and Bowling**: Alternate between batting and bowling in two innings.
- **Score Tracking**: Keep track of the score and target runs to win.
- **Randomized Computer Moves**: The computer's moves are generated randomly for a fair challenge.

## How to Play

1. **Toss**: At the start of the game, choose either "ODD" or "EVEN".
2. **Toss Result**: Input a number between 1 and 6 for the toss. The computer will also choose a random number between 1 and 6. The sum of these numbers will determine the toss result.
    - If the sum matches your choice (odd/even), you win the toss and decide whether to bat or bowl first.
    - If the sum does not match your choice, the computer wins the toss and decides.
3. **Innings**: 
    - If you are batting, input a number between 1 and 6 each turn. The computer will also choose a random number between 1 and 6. If your number matches the computer's number, you are out.
    - If you are bowling, the computer bats and you need to input a number between 1 and 6 to bowl. If the numbers match, the computer is out.
4. **Scoring**: 
    - While batting, your runs are added to your score.
    - While bowling, the computer's runs are added to the target you need to achieve.
5. **Winning**: The game ends after two innings. The player with the higher score wins.


## Example Gameplay

```plaintext
ODD or EVEN ? EVEN
toss podra dei: 3
TOSS : YOU : 3
TOSS : COM : 2
bowl ah bat ah ?? BAT
you : BAT innings 1: 4
you : 4
com : 2
SCORE : 4
...
OUTTTT... COMPUTER WON THE MATCH
```

## Example Gameplay 2

![op](https://github.com/nayakan001/Handcricket-game/assets/137257547/fc82d49a-c0cb-45be-a0b8-32591d0120a6)

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any features, bug fixes, or improvements.




