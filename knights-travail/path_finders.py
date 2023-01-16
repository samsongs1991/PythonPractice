from tree import Node

class KnightPathFinder:
    def __init__(self, pos):
        self._pos = pos
        self._root = Node(pos)
        self._considered_positions = set([pos])

    def find_path(self, pos):
        pass

    def get_valid_moves(self, pos):
        dirs = [
            (-2,-1), (-2,1), (2,-1), (2,1),
            (-1,-2), (1,-2), (-1,2), (1,2),
        ]
        valid_moves = set()
        for d in dirs:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if -1 < new_pos[0] and new_pos[0] < 8 and -1 < new_pos[1] and new_pos[1] < 8:
                valid_moves.add(new_pos)
        return valid_moves

    def new_move_positions(self, pos):
        valid_moves = self.get_valid_moves(pos)
        nonconsidered_positions = set()
        for move in valid_moves:
            if move not in self._considered_positions:
                nonconsidered_positions.add(move)
                self._considered_positions.add(move)
        return nonconsidered_positions
