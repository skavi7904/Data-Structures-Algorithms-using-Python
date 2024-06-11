def process_match(match):
    sets = match.split(',')
    games_won, games_lost, sets_won, sets_lost = 0, 0, 0, 0

    for set_result in sets:
        set_scores = set_result.split('-')
        player_score = int(set_scores[0])
        opponent_score = int(set_scores[1])

        if player_score > opponent_score:
            sets_won += 1
            games_won += player_score
            games_lost += opponent_score
        else:
            sets_lost += 1
            games_won += player_score
            games_lost += opponent_score

    return games_won, games_lost, sets_won, sets_lost


def main():
    players_stats = {}

    while True:
        match = input()
        if match == 'EOF':
            break

        winner, loser, sets_result = map(str.strip, match.split(':'))

        if winner not in players_stats:
            players_stats[winner] = [0, 0, 0, 0, 0, 0]

        games_won, games_lost, sets_won, sets_lost = process_match(sets_result)

        players_stats[winner][0] += 1
        players_stats[loser][1] += 1
        players_stats[winner][2] += sets_won
        players_stats[loser][3] += sets_lost
        players_stats[winner][4] += games_won
        players_stats[loser][5] += games_lost

    sorted_players = sorted(players_stats.items(), key=lambda x: (x[1][0], x[1][2], x[1][4], x[1][5], -x[1][3], -x[1][1]), reverse=True)

    for player, stats in sorted_players:
        print(f'{player} {stats[0]} {stats[1]} {stats[2]} {stats[4]} {stats[3]} {stats[5]}')

