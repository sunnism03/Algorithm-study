n, m = map(int, input().split())

word_set = set()
word_dic = []

for i in range(n):
    word = input()
    
    if word in word_set:
        for i in range(len(word_dic)):
            if word_dic[i][2] == word:
                word_dic[i][0] += 1
                break
    else:
        if len(word) >= m:
            word_dic.append([1, len(word), word])
            word_set.add(word)

word_dic.sort(key=lambda x: (-x[0], -x[1], x[2]))

for i in range(len(word_dic)):
    print(word_dic[i][2])