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


def cleanpoly(poly):
    cleaned_poly = {}
    for coeff, exp in poly:
        if exp in cleaned_poly:
            cleaned_poly[exp] += coeff
        else:
            cleaned_poly[exp] = coeff
    return [(coeff, exp) for exp, coeff in sorted(cleaned_poly.items(), reverse=True) if coeff != 0]


def addpoly(p1, p2):
    cleaned_p1 = cleanpoly(p1)
    cleaned_p2 = cleanpoly(p2)

    result = []
    i, j = 0, 0

    while i < len(cleaned_p1) and j < len(cleaned_p2):
        coeff1, exp1 = cleaned_p1[i]
        coeff2, exp2 = cleaned_p2[j]

        if exp1 > exp2:
            result.append((coeff1, exp1))
            i += 1
        elif exp1 < exp2:
            result.append((coeff2, exp2))
            j += 1
        else:
            result.append((coeff1 + coeff2, exp1))
            i += 1
            j += 1

    result.extend(cleaned_p1[i:])
    result.extend(cleaned_p2[j:])

    return cleanpoly(result)


def multpoly(p1, p2):
    result = []

    for coeff1, exp1 in p1:
        for coeff2, exp2 in p2:
            new_coeff = coeff1 * coeff2
            new_exp = exp1 + exp2
            result.append((new_coeff, new_exp))

    return cleanpoly(result)
