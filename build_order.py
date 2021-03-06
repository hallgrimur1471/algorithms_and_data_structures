#!/usr/bin/env python3.5

def build_order(projects, dependencies):
    i = 0
    dealt_with = set()
    while i < len(projects):
        if projects[i] in dealt_with:
            i += 1
            continue
        if len(dependencies.get(projects[i], "")) == 0:
            dealt_with.add(projects[i])
            continue
        j = i+1
        while (
            (j < len(projects)) and
            (projects[j] != dependencies.get(projects[i], ""))
        ):
            j += 1
        dealt_with.add(projects[i])
        if j == len(projects):
            continue
        tmp = projects[i]
        projects[i] = projects[j]
        projects[j] = tmp
    return projects

projects = ["a", "b", "c", "d", "e", "f"]
#dependencies = [(a, d), (f, b), (b, d), (f, a), (d, c)]
dependencies = {
    "d": "a",
    "b": "f",
    "d": "b",
    "a": "f",
    "c": "d",
}
print(build_order(projects, dependencies))
