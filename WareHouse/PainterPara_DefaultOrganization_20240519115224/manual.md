# Maze Generation App User Manual

## Introduction
The Maze Generation App is a Python application that generates randomized mazes with starting and ending points for users to navigate through. This user manual provides detailed instructions on how to install the necessary dependencies and how to use the app.

## Installation
To use the Maze Generation App, you need to install the following dependencies:

- Python (version 3.6 or higher)
- tkinter (version 8.6 or higher)
- numpy (version 1.19.2 or higher)

You can install these dependencies by running the following command in your terminal:

```
pip install -r requirements.txt
```

## Usage
Once you have installed the dependencies, you can run the Maze Generation App by executing the `main.py` file. Here are the steps to use the app:

1. Open a terminal or command prompt.
2. Navigate to the directory where the `main.py` file is located.
3. Run the following command:

```
python main.py
```

4. The Maze Generation App window will open.
5. Click on the "Generate Maze" button to generate a new maze.
6. The generated maze will be displayed in the app window.
7. The starting point is represented by a green oval, and the ending point is represented by a red oval.
8. You can navigate through the maze by finding a path from the starting point to the ending point.

## Customization
You can customize the dimensions of the maze by modifying the `Maze` class initialization in the `main.py` file. By default, the maze dimensions are set to 10x10. To change the dimensions, modify the following line of code:

```python
self.maze = Maze(10, 10)
```

Replace `10, 10` with your desired dimensions.

## Conclusion
The Maze Generation App provides a simple and interactive way to generate randomized mazes for users to navigate through. Follow the installation and usage instructions in this user manual to start using the app. Enjoy exploring the mazes!