import random
import tkinter as tk
from tkinter import ttk
import numpy as np

WALL = 1
PASSAGE = 0

class Stack:
    def __init__(self):
        self.elements = []
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def push(self, item):
        self.top += 1
        if self.top < len(self.elements):
            self.elements[self.top] = item
        else:
            self.elements.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stos jest pusty")
        item = self.elements[self.top]
        self.top -= 1
        return item

    def size(self):
        return self.top + 1

    def topEl(self):
        if not self.isEmpty():
            return self.elements[self.top]
        return None


class Maze:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.boardSizeX = 2*n + 1
        self.boardSizeY = 2*m + 1
        self.board = np.ones((self.boardSizeX, self.boardSizeY), dtype=int)
        self.visited = np.zeros((n, m), dtype=int)
        self.stack = Stack()

    def makeVisited(self, x, y):
        self.visited[x][y] = 1

    def isVisited(self, x, y):
        return self.visited[x][y] == 1

    def canBreakTheWall(self, x, y):
        if 0 <= x < self.boardSizeX and 0 <= y < self.boardSizeY:
            self.board[x][y] = PASSAGE

    def generatingMaze(self, canvas, cell_size):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        startingPoint = (0, 0)
        self.stack.push(startingPoint)
        self.makeVisited(*startingPoint)

        startingX = 1
        startingY = 1

        self.canBreakTheWall(startingX, startingY)

        while not self.stack.isEmpty():
            currentPoint = self.stack.topEl()
            x, y = currentPoint

            neighbors = []
            for direction in directions:
                nextX, nextY = x + direction[0], y + direction[1]
                if 0 <= nextX < self.n and 0 <= nextY < self.m and not self.isVisited(nextX, nextY):
                    neighbors.append((nextX, nextY))

            if neighbors:
                nextPoint = random.choice(neighbors)
                nextX, nextY = nextPoint

                wallX = 2*x + 1 + (nextX - x)
                wallY = 2*y + 1 + (nextY - y)
                self.canBreakTheWall(wallX, wallY)
                self.canBreakTheWall(2 * nextX + 1, 2 * nextY + 1)

                self.makeVisited(nextX, nextY)
                self.stack.push(nextPoint)
            else:
                self.stack.pop()

            self.GUI(canvas, cell_size)

        # wejscie i wyjscie:
        self.board[1][0] = PASSAGE
        self.board[self.boardSizeX - 2][self.boardSizeY - 1] = PASSAGE

    def GUI(self, canvas, cell_size):
        canvas.delete("all")
        for x in range(self.boardSizeX):
            for y in range(self.boardSizeY):
                if self.board[x][y] == WALL: 
                    canvas.create_rectangle(y * cell_size, x * cell_size, (y + 1) * cell_size, (x + 1) * cell_size, fill="black")
                else:
                    # przejscia
                    canvas.create_rectangle(y * cell_size, x * cell_size, (y + 1) * cell_size, (x + 1) * cell_size, fill="white")
                    
                # wejscie i wyjscie:
                pink = "#FFC0CB"
                if (x == 1 and y == 0):
                    canvas.create_rectangle(y * cell_size, x * cell_size, (y + 1) * cell_size, (x + 1) * cell_size, fill=pink, width=2)
                elif (x == self.boardSizeX - 2 and y == self.boardSizeY - 1):
                    canvas.create_rectangle(y * cell_size, x * cell_size, (y + 1) * cell_size, (x + 1) * cell_size, fill=pink, width=2)

                # numerowanie
                if x % 2 == 1 and y % 2 == 1:
                    canvas.create_text(y * cell_size + cell_size / 2, x * cell_size + cell_size / 2, text=f"({(x // 2) + 1}, {(y // 2) + 1})", font=("Arial", 8), fill="black")

        canvas.update()

def calculateCellSize(n, m):
    wWidth = 800
    wHeight = 600
    
    wCellWidth = wWidth // ((2 * m) + 1)
    wCellHeight = wHeight // ((2 * n) + 1)
    
    return min(wCellWidth, wCellHeight)

def generateMaze():
    n = int(inputN.get())
    m = int(inputM.get())
    if n <= 0 or m <= 0 or n != int(n) or m != int(m):
        raise ValueError("Błędnie wprowadzono wymiary labiryntu")

    cellSize = calculateCellSize(n, m)
    drawingWidth = ((2 * m) + 1) * cellSize
    drawingHeight = ((2 * n) + 1) * cellSize
    canvas.config(width=drawingWidth, height=drawingHeight)
        
    maze = Maze(n, m)
    maze.generatingMaze(canvas, cellSize)


# main:

root = tk.Tk()
root.title("Maze Generator")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Ilość wierszy:").grid(row=0, column=0)
inputN = ttk.Entry(frame)
inputN.grid(row=0, column=1)

tk.Label(frame, text="Ilość kolumn:").grid(row=1, column=0)
inputM = ttk.Entry(frame)
inputM.grid(row=1, column=1)

errorCases = tk.Label(root, text="", fg="red") # informacja o ewentualnych błędach
errorCases.pack()

generateButton = ttk.Button(root, text="Generuj labirynt", command=generateMaze)
generateButton.pack(pady=5)

canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack(pady=10)

root.mainloop()
