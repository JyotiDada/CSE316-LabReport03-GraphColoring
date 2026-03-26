from __future__ import annotations

import argparse
from pathlib import Path


def read_non_empty_lines(file_path: str) -> list[str]:
    return [
        line.strip()
        for line in Path(file_path).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def parse_header(header_line: str) -> tuple[int, int, int]:
    parts = header_line.split()
    if len(parts) != 3:
        raise ValueError(
            "First line must contain exactly three integers: number_of_vertices number_of_edges number_of_colors."
        )

    return tuple(map(int, parts))


def build_graph(vertex_count: int, edge_lines: list[str], expected_edge_count: int) -> list[list[int]]:
    if len(edge_lines) != expected_edge_count:
        raise ValueError("Edge count does not match the number of edges provided.")

    graph = [[0] * vertex_count for _ in range(vertex_count)]

    for line in edge_lines:
        edge = line.split()
        if len(edge) != 2:
            raise ValueError("Each edge line must contain exactly two vertex indices.")

        start, end = map(int, edge)
        if not (0 <= start < vertex_count and 0 <= end < vertex_count):
            raise ValueError("Vertex index out of range.")

        graph[start][end] = 1
        graph[end][start] = 1

    return graph


def parse_input(file_path: str) -> tuple[list[list[int]], int]:
    lines = read_non_empty_lines(file_path)
    if not lines:
        raise ValueError("Input file is empty.")

    vertex_count, edge_count, max_colors = parse_header(lines[0])
    graph = build_graph(vertex_count, lines[1:], edge_count)
    return graph, max_colors


def is_safe(vertex: int, graph: list[list[int]], color: list[int], current_color: int) -> bool:
    for neighbour in range(len(graph)):
        if graph[vertex][neighbour] == 1 and color[neighbour] == current_color:
            return False
    return True


def backtrack(vertex: int, graph: list[list[int]], max_colors: int, color: list[int]) -> bool:
    if vertex == len(graph):
        return True

    for current_color in range(1, max_colors + 1):
        if is_safe(vertex, graph, color, current_color):
            color[vertex] = current_color
            if backtrack(vertex + 1, graph, max_colors, color):
                return True
            color[vertex] = 0

    return False


def solve(graph: list[list[int]], max_colors: int) -> list[int] | None:
    color = [0] * len(graph)
    if backtrack(0, graph, max_colors, color):
        return color
    return None


def print_result(coloring: list[int] | None) -> None:
    if coloring is None:
        print("Not Possible")
    else:
        print("Coloring Possible:", coloring)


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Solve graph coloring using backtracking.")
    parser.add_argument("input_file", help="Path to the input file containing the graph and color limit.")
    return parser


def main() -> None:
    parser = build_argument_parser()
    args = parser.parse_args()

    graph, max_colors = parse_input(args.input_file)
    coloring = solve(graph, max_colors)
    print_result(coloring)


if __name__ == "__main__":
    main()
