# Rougelite

This is a text-based roguelite played by inputting commands into a text promt. 

## Contributing

You can contribute by making a branch and adding your changes. Here is the criterea for contributing:
- Use a tab size of 8 spaces
- Provide comments briefly explaining what your code does
- Use snake case and ALLCAPS when naming variables
    - If the variable is an asset, use lowercase
- Feel free to credit yourself in your code. It's your code after all

## To Do List

In order of importance

- add invalid input catching
- basic assets and menus
- title screen dialouge tree

## GitHub Repository Guide

### Assets

- assets/
  - assets.txt
  - asset_name.py

The assets folder contains all assets used by the game. The assets.txt file contains all assets but mainly things like box formats (It exists because I thought it would be funny to have an assets.txt file.).
An asset is stored as a python variable. They are imported as necessary.

- canvas.txt: used when making assets for the game. The most recent asset will not be removed from the file, meaning you will be able to see the asset that was most recently worked on.
