import random
import os

# Setup table
size = int(input("Choose grid size: "))
os.system('cls')
emptySign = "."
markSign = "O"
noMarkSign = "X"
table = []
undoStack = []

for i in range(size):
    subList = []
    for j in range(size):
        subList.append([random.choice([True, False]), emptySign])
    table.append(list(subList))

def markSlot(coordinates):
    if coordinates == "undo":
        if len(undoStack) > 0:
            table.clear()
            table.extend(undoStack.pop())
        return

    undoStack.append(tableCopy())

    num = 0
    for coordinate in coordinates.split(" "):
        try:
            symbol = markSign
            if coordinate[0] == "~":
                coordinate = coordinate[1:]
                symbol = noMarkSign

            coordinate = coordinate.split(",", 1)
            coordinate[0] = coordinate[0].split(":", 1)
            coordinate[1] = coordinate[1].split(":", 1)

            for i in range(int(coordinate[1][0]), (int(coordinate[1][1]) if len(coordinate[1]) > 1 else int(coordinate[1][0])) + 1):
                for j in range(int(coordinate[0][0]), (int(coordinate[0][1]) if len(coordinate[0]) > 1 else int(coordinate[0][0])) + 1):
                    table[i-1][j-1][1] = symbol

            num += 1

        except:
            print(f"An error has occurred. Only the first {num} command{'s have' if num != 1 else ' has'} been executed.")

def tableCopy():
    copy = []
    for row in table:
        copyRow = []
        for x in row:
            copyRow.append(list(x))
        copy.append(copyRow)
    return copy

def printTable():
    rowData = []
    columnData = []

    for i in range(size):
        curRowData = []
        curStreak = 0
        for j in range(size):
            if table[i][j][0]:
                curStreak += 1
            else:
                curRowData.append(curStreak)
                curStreak = 0
        curRowData.append(curStreak)
        rowData.append(removeAllOf(curRowData, 0))

    for j in range(size):
        curColumnData = []
        curStreak = 0
        for i in range(size):
            if table[i][j][0]:
                curStreak += 1
            else:
                curColumnData.append(curStreak)
                curStreak = 0
        curColumnData.append(curStreak)
        columnData.append(removeAllOf(curColumnData, 0))

    d = ""

    for i in range(size):
        s = ""
        for j in range(size):
            s += table[i][j][1] + " "
        s += "| "
        for k in range(largestLengthInList(rowData)):
            if k < len(rowData[i]):
                s += str(rowData[i][k]) + " "
        d += s + "\n"

    d += "-" * size * 2 + "\n"

    for k in range(largestLengthInList(columnData)):
        s = ""
        for j in range(size):
            if k < len(columnData[j]):
                s += str(columnData[j][k]) + " "
            else:
                s += "  "
        d += s + "\n"

    print(d)

def largestLengthInList(list):
    max = 0
    for sublist in list:
        if len(sublist) > max:
            max = len(sublist)
    return max

def removeAllOf(list, elm):
    i = 0
    while i < len(list):
        if list[i] == elm:
            list.pop(i)
            continue
        i += 1
    return list

def checkWin():
    for row in table:
        for list in row:
            if (list[0] and list[1] != markSign) or (not list[0] and list[1] == markSign):
                return False
    return True

while not checkWin():
    printTable()
    coordinates = input("Enter coordinates: ")
    os.system('cls')
    markSlot(coordinates)

printTable()
print("You win!")
input()