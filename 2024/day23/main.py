from collections import defaultdict
from itertools import combinations


def parse_input():
  file = open('2024/day23/input.txt', 'r')
  lines = file.readlines()
  graph = defaultdict(lambda: set())
  
  for line in lines: 
    line = line.strip()
    left, right = line.split('-')
    left = left.strip()
    right = right.strip()
    
    graph[left].add(right)
    graph[right].add(left)
  
  return graph

def part_one():
  graph = parse_input()
  result = set()
  for a in graph.keys():
    for b in graph[a]:
      for c in graph[b]:
        if a in graph[c]:
          if a.startswith('t') or b.startswith('t') or c.startswith('t'):
            key = [a, b , c]
            key.sort()
            result.add(','.join(key))
   
  # for r in result:
  #   print(r)

  return len(result)

# def is_clique(graph, vertices):
#     for i in range(len(vertices)):
#         for j in range(i + 1, len(vertices)):
#             if vertices[j] not in graph[vertices[i]]:
#                 return False
#     return True


# def find_max_clique(graph):
#     max_clique = []
#     vertices = list(graph.keys())
    
#     # Test all possible subsets of vertices
#     for size in range(1, len(vertices) + 1):
#         for subset in combinations(vertices, size):
#             if is_clique(graph, subset):
#                 if len(subset) > len(max_clique):
#                     max_clique = list(subset)
    
#     return max_clique
  


def part_two():
  graph = parse_input()
  # https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
  def bron_kerbosch(r, p, x, cliques):
    if not p and not x:
      cliques.append(r)
      return 
    u = p | x  # algorithm with pivot -> faster version
    u = u.pop() # algorithm says to pick a pivot not specifically says which one  ¯\_(ツ)_/¯
    
    # for v in p.copy(): without pivot
    for v in p - graph[u]:
      bron_kerbosch(r | {v}, p & graph[v], x & graph[v], cliques)
      p.remove(v)
      x.add(v)
 


  cliques = []
  bron_kerbosch(set(), set(graph.keys()), set(), cliques)
  
  max_clique = list(max(cliques, key=len))
  max_clique.sort()
  return ','.join(max_clique)


print('Solution 1.', part_one())
print('Solution 2.', part_two())