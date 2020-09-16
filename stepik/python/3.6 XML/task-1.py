from xml.etree import ElementTree

color_score = {
    'red': 0,
    'green': 0,
    'blue': 0
}

def check_color(root, score=1):
    color = root.attrib['color']
    color_score[color] += score
    for child in root:
        check_color(child, score+1)


string = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'

root = ElementTree.fromstring(string)

print(root)
print(root.tag, root.attrib, '\n')

check_color(root)

print(color_score)