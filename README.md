# Purpose

This repo is a starting template for an application or game using Pygame.

main.py contains the App class that provides the Pygame setup and establishes a game loop from which update() and draw() are called on the App and on the Game object created from the Game class in game.py.

One should be able to clone this repo and immediately begin implementing their game logic in the Game class update() and draw() methods.

# Usage

- Clone this repo
- Create a virtual environment
- Activate the virtual environment
- Install the dependencies listed in requirements.txt

```
python -m venv venv
venv\Scripts\activate.bat
# or
source ./venv/bin/activate
pip install -r requirements.txt
python main.py
```