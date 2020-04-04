# js = [
#     {
#         'name': 'A',
#         'parents': []
#     },
#     {
#         'name': 'B',
#         'parents': ['A', 'C']
#     },
#     {
#         'name': 'C',
#         'parents': ['A']
#     }
# ]

js = [{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]

data, data2 = dict(), dict()

for node in js:
    data[node['name']] = node['parents']
    data2[node['name']] = 0

print(data)
print()
print(data2)

def count_childs(node, parents):
    for parent in parents:
        if parent not in visited:
            try:
                data2[parent] += 1
            except:
                data2[parent] = 1
            visited.add(parent)
        count_childs(parent, data[parent])

for node in data:
    visited = set()
    count_childs(node, data[node])


for node in data2:
    data2[node] += 1

print()

for key in sorted(data2):
    print(f'{key} : {data2[key]}')
