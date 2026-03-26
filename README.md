# Graph Coloring using Backtracking

## Problem Description
Determine whether a graph can be colored using K colors so that no two adjacent vertices share the same color.

## Algorithm
- Use backtracking
- Assign colors vertex by vertex
- Check whether a color is safe before assigning it
- Backtrack when a conflict appears

## Complexity
- Time: O(K^N)
- Space: O(N)

## Project Structure
- `code/graph_coloring.py`
- `input/case1.txt`
- `input/case2.txt`
- `output/`

## Input Format
- First line: `number_of_vertices number_of_edges number_of_colors`
- Next M lines: edges written as `u v`

## Run
```bash
python code/graph_coloring.py input/case1.txt
python code/graph_coloring.py input/case2.txt
```

## Output
- Case 1: Coloring Possible
- Case 2: Not Possible
