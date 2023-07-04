# finalCapstone
Minesweeper is a single player puzzle game in which the player tries to uncover as many squares as possible without clicking on a mine. 
The numbers in the uncovered squares indicate the number of mines surrounding it.
This program takes inspiration from the minesweeper game.

## Contents
1. Description
2. Installation/Usage

## 1. Description
This code defines a function 'minesweeper(grid)' which is a 2D list consisting of (#) and (-), where (#) represents a mine and (-) represents a mine-free spot.
The function returns a grid where each (-) is repaced by a digit, indicating the number of mines immediately adjacent to the spot i.e. horizontally, vertically and diagonally. When checking adjacent positions in the grid, the edges of the grid are taken into account.

Input example:

[["-", "-", "-", "#", "#"],

 ["-", "#", "-", "-", "-"],
 
 ["-", "-", "#", "-", "-"],
 
 ["-", "#", "#", "-", "-"],
 
 ["-", "-", "-", "-", "-"]]

 Output example:
 
 [["1", "1", "2", "#", "#"],
 
  ["1", "#", "3", "3", "2"],
  
  ["2", "4", "#", "2", "0"],
  
  ["1", "#", "#", "2", "0"],
  
  ["1", "2", "2", "1", "0"]]


The program includes use of the enumerate function in Python to keep track of the index points and values without having to create a count variable and explicitly iterate the count variable to keep track of the current row or column index.

## 2. Installation/Usage
minesweeper.py is written in Visual Studio Code for Python but any other code editor that supports Python will also work. No packages required.

![image](https://github.com/amaria24-max/finalCapstone/assets/127986993/d1a931d1-3704-4907-9453-51476afa71b8)

The program follows the structure of the description above; the user runs the program to get the expected outputs.
The program can be altered to allow for different sized grids which would require adjustments to the ranges.
