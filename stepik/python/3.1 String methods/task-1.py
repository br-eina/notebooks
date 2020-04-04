def main():
    s, a, b = input(), input(), input()

    ans = 'Impossible'

    if a not in s:
        print(0)
        return
    elif a in b:
        print(ans)
        return

    for i in range(1000):
        new_s = s.replace(a, b)
        if s == new_s:
            ans = i
            break
        s = new_s
    print(ans)

main()