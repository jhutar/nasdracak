import copy
import statistics

values = {
    "sila": [],
    "obratnost": [],
    "inteligence": [],
    "vule": [],
}

def doit(points, values, recurse=0):
    # print(f"{' ' * 4 * recurse}Working on {values=} with {points=}")

    can_not_add = []

    for k in values.keys():
        price = len(values[k]) + 1
        if price > points:
            can_not_add.append(True)
        else:
            can_not_add.append(False)
            # print(f"{' ' * 4 * recurse}Incrementing {k}")
            values_new = copy.deepcopy(values)
            values_new[k].append(1)
            for v in doit(points - price, values_new, recurse + 1):
                yield v

    # Could not add to neither of 4 keys
    if can_not_add == [True, True, True, True]:
        yield values

    # print(f"{' ' * 4 * recurse}End of loop")

values_counts = copy.deepcopy(values)
sum_counts = []
min_in_one_counts = []
max_in_one_counts = []

for v in doit(14, values):
    for k in values_counts.keys():
        values_counts[k].append(sum(v[k]))
        sum_counts.append(sum([sum(i) for i in v.values()]))
        min_in_one_counts.append(min([sum(i) for i in v.values()]))
        max_in_one_counts.append(max([sum(i) for i in v.values()]))

for k in values_counts.keys():
    print(f"Min, avg and max for '{k}': {min(values_counts[k])}, {statistics.mean(values_counts[k]):.2f}, {max(values_counts[k])}")
print(f"Totals min, avg and max: {min(sum_counts)}, {statistics.mean(sum_counts)}, {max(sum_counts)}")
print(f"Average min and max in one: {statistics.mean(min_in_one_counts):.2f} (min {min(min_in_one_counts)}) - {statistics.mean(max_in_one_counts):.2f}, (max {max(max_in_one_counts)})")
