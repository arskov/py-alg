import os
import sys

#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    if not indexes or not queries:
        return [[]]
    res_res = []
    
    def dfs(cur_index, k, level, res):
        if cur_index == -1:
            return
        _left = indexes[cur_index - 1][0]
        _right = indexes[cur_index - 1][1]
        if level % k == 0:
            _left, _right = _right, _left
            indexes[cur_index - 1][0] = _left
            indexes[cur_index - 1][1] = _right
        dfs(_left, k, level + 1, res)
        res.append(cur_index)
        dfs(_right, k, level + 1, res)
    
    for q in queries:
        in_order = []
        dfs(1, q, 1, in_order)
        res_res.append(in_order)
        
    return res_res
        
if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    with open(sys.path[0] + '/swap_nodes_input.txt', 'r') as in_file, \
         open(sys.path[0] + '/swap_nodes_out_test.txt', 'w') as out_file:

        n = int(in_file.readline())

        indexes = []

        for _ in range(n):
            indexes.append(list(map(int, in_file.readline().rstrip().split())))

        queries_count = int(in_file.readline())

        queries = []

        for _ in range(queries_count):
            queries_item = int(in_file.readline())
            queries.append(queries_item)

        result = swapNodes(indexes, queries)

        out_file.write('\n'.join([' '.join(map(str, x)) for x in result]))

    import filecmp
    print(filecmp.cmp(sys.path[0] + '/swap_nodes_out_test.txt', sys.path[0] + '/swap_nodes_out_assert.txt'))
