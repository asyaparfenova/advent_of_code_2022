import numpy as np

def parse_data(input_file):
    mtrx = np.loadtxt(input_file, dtype=str)
    mtrx = np.array([list(a) for a in mtrx]).astype(int)
    return mtrx

def part_one(mtrx):
    count = 2*(len(mtrx) + len(mtrx[0]) - 2)
    for x in range(1,len(mtrx)-1):
        for y in range(1,len(mtrx[0])-1):
            c1 = (mtrx[x,y] > max(mtrx[:x,y]))
            c2 = (mtrx[x, y] > max(mtrx[x+1:, y]))
            c3 = (mtrx[x, y] > max(mtrx[x, :y]))
            c4 = (mtrx[x, y] > max(mtrx[x, y+1:]))
            if c1 or c2 or c3 or c4:
                count += 1
    return count

def measure_view(tree, row):
    count = 0
    for i in row:
        count += 1
        if i >= tree:
            break
    return count

def part_two(mtrx):
    max_score = 1
    for x in range(1,len(mtrx)-1):
        for y in range(1,len(mtrx[0])-1):
            tree = mtrx[x,y]
            up_count = measure_view(tree, np.flip(mtrx[:x,y]))
            down_count = measure_view(tree, mtrx[x+1:, y])
            left_count = measure_view(tree, np.flip(mtrx[x, :y]))
            right_count = measure_view(tree, mtrx[x, y+1:])
            tree_score = up_count * down_count * left_count * right_count
            if tree_score > max_score:
                max_score = tree_score
    return max_score

if __name__ == "__main__":
    mtrx = parse_data("input.txt")
    print(f"The answer for the 1st task is: {part_one(mtrx)}")
    print(f"The answer for the 2nd task is: {part_two(mtrx)}")
