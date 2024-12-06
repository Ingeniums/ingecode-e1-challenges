from functools import cmp_to_key
import sys
products = {}

complaints = []
with open(sys.argv[1], "r") as file:
    complaints = file.readlines();

scores = {}

def get_score(rank):
    if rank == 1:
        return 4
    elif rank == 2:
        return 3
    elif rank == 3:
        return 2
    elif rank == 4:
        return 1
    else:
        return 0.5

def get_complaints(complaints_str):
    # ignore first line indicating number of complaints
    complaints_str = complaints_str[1:]
    complaints = []
    for c in complaints_str:
        if not " " in c:
            complaints.append([])
            continue
        complaints[-1].append(list(map(lambda x: int(x), c.split())))
    return complaints

def get_files_list(complaint):
    # remove line feed
    visited = 0
    i = 0
    while visited < len(complaint):
        visited += 1
        # update the score of the product at the current rank
        if complaint[i][1] in scores.keys():
            scores[complaint[i][1]] += get_score(visited)
        else:
            scores[complaint[i][1]] = get_score(visited)
        # jump to tuple at rank (-1 to account for indexing starting at 0 rather than 1)
        i = complaint[i][0] - 1

for complaint in get_complaints(complaints):
    get_files_list(complaint)


def compare(id1, id2):
    if scores[id1] < scores[id2]:
        return -1
    elif scores[id1] > scores[id2]:
        return 1
    else:
        return id2 - id1
scores_sorted = sorted(scores.keys(), key=cmp_to_key(compare), reverse=True)

for id in scores_sorted[:3]:
    print(f"id: {id}, score: {scores[id]}")

print(abs(scores_sorted[0] - scores_sorted[1]) * scores_sorted[2])
