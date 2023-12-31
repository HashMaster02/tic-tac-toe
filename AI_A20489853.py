"""
This class acts as a container for the AI. It contains both the algorithm implementations
and the utility function.
"""


class AI:

    def __init__(self):
        self.utility = {'X': 1, 'O': -1, 'TIE': 0}
        self.total_nodes = 0

    def min_max(self, game):
        self.total_nodes += 1
        # check terminal state
        is_winner = game.has_ended()
        if is_winner is not None:
            return None, self.calculate_utility(is_winner, game.board.available_moves)

        # Max-Player (X) i.e. higher values are advantageous
        if game.current_player == "X":
            (move, value) = (None, -10000)
            for action in game.board.available_moves:
                game.play_move(action)
                game.next_player()
                (_, new_value) = self.min_max(game)
                game.undo_move(action)  # undo the previous move before trying the rest (deal with side effects)

                if new_value > value:
                    (move, value) = (action, new_value)

            return move, value

        # Min-Player (X) i.e. lower values are advantageous
        if game.current_player == "O":
            (move, value) = (None, 10000)
            for action in game.board.available_moves:
                game.play_move(action)
                game.next_player()
                (_, new_value) = self.min_max(game)
                game.undo_move(action)  # undo the previous move before trying the rest (deal with side effects)

                if new_value < value:
                    (move, value) = (action, new_value)

            return move, value

    def alpha_beta_pruning(self, game, alpha, beta):
        self.total_nodes += 1
        # check terminal state
        is_winner = game.has_ended()
        if is_winner is not None:
            return None, self.calculate_utility(is_winner, game.board.available_moves)

        # Max-Player (X) i.e. higher values are advantageous
        if game.current_player == "X":
            (move, value) = (None, -10000)
            for action in game.board.available_moves:
                game.play_move(action)
                game.next_player()
                (_, new_value) = self.alpha_beta_pruning(game, alpha, beta)
                game.undo_move(action)  # undo the previous move before trying the rest (deal with side effects)
                alpha = max(alpha, new_value)

                if new_value > value:
                    (move, value) = (action, new_value)
                if beta <= alpha:
                    break

            return move, value

        # Min-Player (X) i.e. lower values are advantageous
        if game.current_player == "O":
            (move, value) = (None, 10000)
            for action in game.board.available_moves:
                game.play_move(action)
                game.next_player()
                (_, new_value) = self.alpha_beta_pruning(game, alpha, beta)
                game.undo_move(action)  # undo the previous move before trying the rest (deal with side effects)
                beta = min(beta, new_value)
                if new_value < value:
                    (move, value) = (action, new_value)
                if beta <= alpha:
                    break

            return move, value

    def calculate_utility(self, player, remaining_moves):
        """
        The utility formula below can vary which can change the decision of the AI for certain board configurations.
        Try using one of these and see if you can notice a (subtle) difference.

        Formula 1: self.utility[player]
        Formula 2: self.utility[player] * (len(remaining_moves))
        Formula 3: self.utility[player] * (len(remaining_moves) + 1)
        """

        return self.utility[player]
