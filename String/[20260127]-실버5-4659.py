#import sys
#input = sys.stdin.readline

vowel = ["a", "e", "i", "o", "u"]

while True :
    word = input()
    if word == "end":
        break
    
    # 모음 포함 여부
    vo_cnt = 0
    for i in word:
        if i in vowel:
            vo_cnt += 1
    
    if vo_cnt <= 0:
        print(f'<{word}> is not acceptable.')
        continue
    
    # 모음/자음 연속 3개 여부
    x = 0
    for i in range(len(word)-2):
        if word[i] in vowel and word[i+1] in vowel and word[i+2] in vowel :
            x = 1 
        elif not(word[i] in vowel) and not(word[i+1]in vowel) and not(word[i+2] in vowel) :
            x = 1 
    if x == 1 :
        print(f'<{word}> is not acceptable.')
        continue
    
    # 같은 글자 연속 2개 여부(ee, oo 제외)
    y = 0
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            if word[i] == 'e' or word[i] == 'o':
                continue
            else:
                y = 1
    if y == 1:
        print(f'<{word}> is not acceptable.')
        continue
    
    print(f'<{word}> is acceptable.')