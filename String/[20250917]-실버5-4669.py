vowels = ['a', 'e', 'i', 'o', 'u']

def is_acceptable(pw: str) -> bool:
    # 1. 모음 포함 여부
    if not any(ch in vowels for ch in pw):
        return False
    
    # 2. 모음/자음 3개 연속 체크
    for i in range(len(pw) - 2):
        if (pw[i] in vowels and pw[i+1] in vowels and pw[i+2] in vowels) or \
           (pw[i] not in vowels and pw[i+1] not in vowels and pw[i+2] not in vowels):
            return False
    
    # 3. 같은 글자 연속 (ee, oo는 허용)
    for i in range(len(pw) - 1):
        if pw[i] == pw[i+1] and pw[i] not in ['e', 'o']:
            return False
    
    return True


while True:
    pw = input().strip()
    if pw == "end":
        break
    
    if is_acceptable(pw):
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")
