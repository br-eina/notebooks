base = {}
already_checked = set()

def test(child):
    try:
        if base[child] == None:
            return 'Not to delete'
    except KeyError:
        return 'Not to delete'

    if base[child] in already_checked or child in already_checked:
        return 'Delete'

    for cl in base[child]:
        if test(cl) == 'Delete':
            return 'Delete'

    return 'Not to delete'

for com in [input().split() for i in range(int(input()))]:
    base[com[0]] = None if len(com) == 1 else com[2:len(com)]

trig = 0
for com in [input() for i in range(int(input()))]:
    if test(com) == 'Delete':
        trig +=1
        if trig == 1:
            print('----------')
        print(com)
    already_checked.add(com)






# print()
# print(base)

# print()
# print(already_checked)






# a = input().split()
# print('\n', a[0])
# print(a[1])
# print(a[2])
