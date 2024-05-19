# Maze Generation App User Manual

Welcome to the Maze Generation App! This user manual will guide you through the installation process and explain how to use the app to generate randomized mazes.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Generating Mazes](#generating-mazes)
4. [Example Code](#example-code)
5. [Conclusion](#conclusion)

## 1. Installation <a name="installation"></a>

To use the Maze Generation App, you need to have Python installed on your system. Follow these steps to install the necessary dependencies:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have saved the `main.py` and `maze.py` files.
3. Run the following command to install the required dependencies:

   ```shell
   pip install random
   ```

4. Once the installation is complete, you are ready to use the Maze Generation App!

## 2. Usage <a name="usage"></a>

To use the Maze Generation App, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have saved the `main.py` and `maze.py` files.
3. Run the following command to execute the app:

   ```shell
   python main.py
   ```

4. The app will generate a randomized maze and display it in the terminal.

## 3. Generating Mazes <a name="generating-mazes"></a>

The Maze Generation App uses a depth-first search algorithm to generate randomized mazes. The `Maze` class in the `maze.py` file handles the maze generation process.

To customize the size of the maze, you can modify the parameters passed to the `Maze` constructor in the `main.py` file. For example, to create a maze with 15 rows and 20 columns, change the following line of code:

```python
maze = Maze(10, 10)
```

to:

```python
maze = Maze(15, 20)
```

## 4. Example Code <a name="example-code"></a>

Here is an example of how to use the Maze Generation App:

```python
from maze import Maze

# Create a new maze with 10 rows and 10 columns
maze = Maze(10, 10)

# Print the maze grid
for row in maze.grid:
    print(row)
```

This code will generate a maze with 10 rows and 10 columns and print the maze grid.

## 5. Conclusion <a name="conclusion"></a>

Congratulations! You have successfully installed and used the Maze Generation App. You can now generate randomized mazes and customize their size according to your needs. Have fun navigating through the mazes!