import math

def minimax_alpha_beta(node, depth, alpha, beta, is_maximizing):
    # Base case: if we hit a leaf node (an integer value) or max depth
    if isinstance(node, int) or depth == 0:
        return node

    if is_maximizing:
        max_eval = -math.inf
        for child in node:
            eval_score = minimax_alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                print(f"Pruned at Maximizer: alpha ({alpha}) >= beta ({beta})")
                break  # Beta cutoff
        return max_eval

    else:
        min_eval = math.inf
        for child in node:
            eval_score = minimax_alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                print(f"Pruned at Minimizer: beta ({beta}) <= alpha ({alpha})")
                break  # Alpha cutoff
        return min_eval


# Example Game Tree:
# Depth 0: Root (Max)
# Depth 1: Two children (Min)
# Depth 2: Terminal leaf values
game_tree = [
    [3, 5],     # First branch evaluated by Min
    [6, 9]      # Second branch evaluated by Min
]

# Run the search starting at the root
optimal_value = minimax_alpha_beta(
    node=game_tree,
    depth=2,
    alpha=-math.inf,
    beta=math.inf,
    is_maximizing=True
)

print(f"Optimal Root Value: {optimal_value}")
