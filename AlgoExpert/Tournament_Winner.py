# Time Complexty: O(n) where n=len(competitions)
# Space Complexty: O(n) where n=len(competitions)

def tournamentWinner(competitions, results):
    curr_top_score = 0
    curr_top_team = ""
    scores = {}

    for i in range(len(competitions)):
        winner_i = 1 - results[i]
        winner = competitions[i][winner_i]

        if winner not in scores:
            scores[winner] = 0
        scores[winner] += 3

        if curr_top_score < scores[winner]:
            curr_top_score = scores[winner]
            curr_top_team = winner

    return curr_top_team
