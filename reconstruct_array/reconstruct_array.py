from collections import defaultdict

def create_graph(adjacent_pairs):
    neighbors = defaultdict(list)
    for u, v in adjacent_pairs:
        neighbors[u].append(v)
        neighbors[v].append(u)

    return neighbors

def topo_dfs(graph):
    candidates = (u for u, v in graph.items() if len(v) == 1)

    def traverser():
        prev = None
        cur = next(candidates)
        seen = set()

        def dfs_next(cur):
            return next(filter(lambda x: x != prev, graph[cur]), None)

        topo = filter(lambda x: x not in seen, candidates)

        while cur:
            seen.add(cur)
            yield cur
            nxt = dfs_next(cur) or next(topo, None)
            prev = cur
            cur = nxt

    return list(traverser())


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        return topo_dfs(create_graph(adjacentPairs))