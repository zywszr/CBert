

def print_sentence(l, r, words, suffix=''):
    # print("l: {}, r: {}".format(l, r))
    for i in range(l, r):
        if words[i] == '':
            continue
        f.write(words[i] + ' ')
    # f.write("++")
    f.write(words[r] + '\n')

f = open("./wiki.train.raw.txt", "r")
# f = open("./wiki.test.txt", "r")
# f = open("./test_data.txt", "r")
lines = f.readlines()
f.close()

first = True
f = open("./raw_data.txt", "w")
for i, line in enumerate(lines):
    # print("len(line{}): {}".format(i, len(line)))
    # print(line)
    if len(line) <= 2:  # blank lines
        continue
    if line[0:3] == ' = ':  # new document
        if line.count('=') == 2:
            if not first:
                f.write('\n')
            first = False
        continue

    words = line.split(' ')
    # print(words[-1])
    if words[-1] == '"' + '\n':
        # print('********true')
        words[-1] = '"'
        words.append('\n')
    # print(words)
    # print("words[0]: {}".format(words[0]))
    # print("words[1]: {}".format(words[1]))
    # print("words[len - 1]: {}".format(words[-1]))

    l = 0
    r = 0
    n_broad = 0
    quotation = False
    quotation_chinese = 0
    end = False
    while r < len(words) - 1:
        word = words[r]
        if word == '':
            r = r + 1
            if l == r - 1:
                l = r
            continue
        if word == '.' or word == '?' or word == '!':
            end = True
        if word == '(':
            n_broad += 1
        if word == ')':
            n_broad -= 1
        # print(word)
        if word == '"':
            # print("quotation_before: {}".format(quotation))
            quotation = not quotation
            # print("quotation_after: {}".format(quotation))
        if word == '“':
            quotation_chinese += 1
        if word == '”':
            quotation_chinese -= 1

        if n_broad == 0 and not quotation and quotation_chinese == 0 and end:
            # print(word, end)
            if word == ')' and words[l] != '(':
                end = False
                r += 1
                continue
            if words[r + 1] == ',' or words[r + 1] == '!' or words[r + 1] == '?' or words[r + 1] == '.':
                end = False
                r += 1
                continue

            end = False
            print_sentence(l, r, words)
            r += 1
            l = r
        else:
            r += 1
    if l != r:
        print_sentence(l, r - 1, words)


# . r"
# ! r"
# ? r"

# .
# ?
# !

# (
# . )
# replace "" with l" & r"
    '''
    list1 = line.split('"')
    line = list1[0]
    for i in range(1, len(list1)):
        if i & 1 == 1:
            line = line + 'l"' + list1[i]
        else:
            line = line + 'r"' + list1[i]
    '''