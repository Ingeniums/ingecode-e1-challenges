import random
import sys

class Constraint:
    def __init__(self, ids, row_calc) -> None:
        self.ids = ids
        self.row_calc = row_calc

num_complaints = 8000
id1 = 153289535706703
id2 = 134322867652075
id3 = 129670661363975
constraints = [
    Constraint(id1, lambda total: int(total * (3 / 8))),
    Constraint([id2, id3], lambda total: int(total * (3 / 8))),
]

forbidden_ids = []
for c in constraints:
    if type(c.ids) is list:
        forbidden_ids.extend(c.ids)
    else:
        forbidden_ids.append(c.ids)

def get_rand_id():
    return random.randint(95783283599628, 189249393493289)

def generate_id(complaint_product_ids):
    id = get_rand_id()
    while id in complaint_product_ids or id in forbidden_ids:
        id = get_rand_id()
    complaint_product_ids.append(id)
    return id

"""
Generates a complaint with the specified id appearing in the specified order. 
Length specifies the number of files in the complaint, and cannot be less than order.
If order is -1 then a random complaint is generated not necessarily containing id.
"""
def generate_complaint_with_fixed_order(id, order, length):
    if length < order:
        raise ValueError("order cannot be greater than length")
    index = 0
    files = [""] * length
    orders = list(range(2, length + 1))
    random.shuffle(orders)
    chosen_ids = []
    for i in range(length):
        # only last remaining
        chosen = orders[i] if len(chosen_ids) < length - 1 else -1
        if (i + 1) == order:
            files[index] = f"{chosen} {id}"
            chosen_ids.append(id)
        else:
            files[index] = f"{chosen} {generate_id(chosen_ids)}"
        index = chosen - 1
    return files

def generate_complaint_equal_order_for(ids):
    order = get_unfair_order()
    results = []
    for id in ids:
        results.append(generate_complaint_with_fixed_order(id, order, random.randint(order + 1, 30)))
    return results

def get_unfair_order():
    return random.randint(1, 6)

def generate_complaints(num_complaints, constraints):
    complaints = []
    remaining_complaints = num_complaints
    for constraint in constraints:
        rows = constraint.row_calc(num_complaints)
        if type(constraint.ids) is list:
            remaining_complaints -= (rows // len(constraint.ids)) * len(constraint.ids)
            pairs = rows // len(constraint.ids)
            for _ in range(pairs):
                complaints.extend(generate_complaint_equal_order_for(constraint.ids))
        else:
            remaining_complaints -= rows
            order = get_unfair_order()
            for _ in range(rows):
                complaints.append(generate_complaint_with_fixed_order(constraint.ids, order, random.randint(order + 1, 30)))
    for _ in range(remaining_complaints):
        complaints.append(generate_complaint_with_fixed_order(0, -1, random.randint(15, 30)))
    shuffle_rounds = 2
    for _ in range(shuffle_rounds):
        random.shuffle(complaints)
    return list(map(lambda c: f"{len(c)}\n" + "\n".join(c), complaints))

with open(sys.argv[1], "w") as file:
    file.write(f"{num_complaints}\n" + "\n".join(generate_complaints(num_complaints, constraints)))
