# Algorythm return the smallest uniq string deleting unnecessary letters

word = "cbacdcbc"


def tsus(word):
    cnt = [0 for _ in range(26)]
    v = [False for _ in range(26)]
    for l in word:
        cnt[ord(l) - 97] += 1
    stack = []
    stack.append(word[0])
    cnt[ord(word[0]) - 97] -= 1
    for i in range(1, len(word)):
        l = word[i]
        ns = len(stack)
        nl = ord(l)
        if cnt[ord(stack[ns - 1]) - 97] != 0:
            if nl < ord(stack[ns - 1]):
                v[ord(stack[ns - 1]) - 97] = False
                stack.pop(ns - 1)
                stack.append(l)
                cnt[ord(l) - 97] -= 1
                v[ord(l) - 97] = True
            else:
                if cnt[ord(l) - 97] == 1:
                    stack.append(l)
                    cnt[ord(l) - 97] -= 1
                    v[ord(l) - 97] = True

        else:
            if not v[ord(l) - 97]:
                stack.append(l)
                cnt[ord(l) - 97] -= 1
                v[ord(l) - 97] = True
                continue

    return stack


print(tsus(word))
