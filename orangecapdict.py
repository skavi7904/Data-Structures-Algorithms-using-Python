def orangecap(d):
    player_scores = {}

    for match_scores in d.values():
        for player, score in match_scores.items():
            if player in player_scores:
                player_scores[player] += score
            else:
                player_scores[player] = score

    top_player = max(player_scores, key=player_scores.get)
    top_score = player_scores[top_player]

    return top_player, top_score

print(orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}))
