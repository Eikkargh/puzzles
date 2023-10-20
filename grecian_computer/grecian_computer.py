import numpy as np

puzzle = np.array([[[0 , 0 , 0 , 3 ],
                   [0 , 0 , 0 , 0 ],
                   [0 , 0 , 0 , 6 ],
                   [0 , 0 , 0 , 0 ],
                   [0 , 0 , 0 , 10],
                   [0 , 0 , 0 , 0 ],
                   [0 , 0 , 0 , 7 ],
                   [0 , 0 , 0 , 0 ],
                   [0 , 0 , 0 , 15],
                   [0 , 0 , 0 , 0 ],
                   [0 , 0 , 0 , 8 ],
                   [0 , 0 , 0 , 0 ]],
                  [[0 , 0 , 4 , 7 ],
                   [0 , 0 , 0 , 3 ],
                   [0 , 0 , 7 , 0 ],
                   [0 , 0 , 15, 6 ],
                   [0 , 0 , 0 , 0 ],
                   [0 , 0 , 0 , 11],
                   [0 , 0 , 14, 11],
                   [0 , 0 , 0 , 6 ],
                   [0 , 0 , 9 , 11],
                   [0 , 0 , 0 , 0 ],
                   [0 , 0 , 12, 6 ],
                   [0 , 0 , 0 , 17]],
                  [[0 , 5 , 21, 9 ],
                   [0 , 0 , 6 , 13],
                   [0 , 10, 15, 9 ],
                   [0 , 0 , 4 , 7 ],
                   [0 , 8 , 9 , 13],
                   [0 , 0 , 18, 21],
                   [0 , 22, 11, 17],
                   [0 , 0 , 26, 4 ],
                   [0 , 16, 14, 5 ],
                   [0 , 0 , 1 , 0 ],
                   [0 , 9 , 12, 7 ],
                   [0 , 0 , 0 , 8 ]],
                  [[1 , 3 , 9 , 7 ],
                   [0 , 26, 20, 0 ],
                   [9 , 6 , 12, 9 ],
                   [0 , 0 , 3 , 0 ],
                   [12, 2 , 6 , 7 ],
                   [0 , 13, 0 , 14],
                   [6 , 9 , 14, 11],
                   [0 , 0 , 12, 0 ],
                   [10, 17, 3 , 8 ],
                   [0 , 19, 8 , 0 ],
                   [10, 3 , 9 , 16],
                   [0 , 12, 0 , 2 ]],
                  [[3 , 4 , 5 , 11],
                   [4 , 6 , 6 , 14],
                   [12, 6 , 7 , 11],
                   [2 , 3 , 8 , 14],
                   [5 , 3 , 9 , 11],
                   [10, 14, 10, 14],
                   [7 , 14, 11, 14],
                   [16, 21, 12, 11],
                   [8 , 21, 13, 14],
                   [7 , 9 , 14, 11],
                   [8 , 9 , 15, 14],
                   [8 , 4 , 4 , 11]]])
solved = False

def solveCheck(nums):
    for n in range(len(nums)):
        total = sum(nums[n])
        if total != 42:
            return False
    return True

def checkVisible():
    global solved
    visibleNums = np.zeros((12, 4), dtype=int)
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            for k, v in enumerate(puzzle[i][j]):
                if v != 0 and visibleNums[j][k] == 0:
                    visibleNums[j][k] = v  
    solved = solveCheck(visibleNums)
    if solved:
        print("\nSolution found:")
        print(puzzle)
        
def rotateDisk(d):
    disk = puzzle[d]
    disk = np.roll(disk, 1, axis=0)
    puzzle[d] = disk
    checkVisible()
    
def diskSelect():
    count = 0
    for _disk3 in range(0,11):
        for _disk2 in range(0,11):
            for _disk1 in range(0,11):
                for _disk0 in range(0,11):
                    rotateDisk(0)
                    if solved:
                        return
                    count += 1
                    print("No solution count:%d" % count, end="\r")
                rotateDisk(1)
                if solved:
                    return
                count += 1
                print("No solution count:%d" % count, end="\r")
            rotateDisk(2)
            if solved:
                return
            count += 1
            print("No solution count:%d" % count, end="\r")
        rotateDisk(3)
        if solved:
            return
        count += 1
        print("No solution count:%d" % count, end="\r")

print("Grecian Computer Solver")
diskSelect()


 
