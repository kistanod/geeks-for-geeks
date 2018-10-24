# https://practice.geeksforgeeks.org/problems/winner-of-an-election-where-votes-are-represented-as-candidate-names/0

def find_winners(candidates):
    winner_votes = max(candidates.values())
    winners = []
    for name, votes in candidates.items():
        if votes == winner_votes:
            winners.append(name)
    return winners

def count_votes(votes):
    candidates = dict.fromkeys(set(votes), 0)
    for vote in votes:
        candidates[vote] += 1
    winners = find_winners(candidates)
    print("{} {}".format(min(winners), max(candidates.values())))
    
    
for testcase in range(int(input())):
    N = int(input())
    votes = list(input().split())
    count_votes(votes)
