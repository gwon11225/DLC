def end(command):
    if command == '0':
        return True
def inCheck(command:str,good_word:list,bad_word:list,hang):
    for i in good_word:
        if i in command:
            if i == 'DLC' or i == '두카미' or i == '문주호':
                hang += 100*command.count(i)
            hang += 10*command.count(i)
    for i in bad_word:
        if i in command:
            if i == '방과후' or i == '플루트':
                hang -= 20*command.count(i)
            hang -= 10*command.count(i)
    return hang
good_word = ['자습', '급식', '회식', '게임', '운동', '체육', '자율', '용돈', '수면', '음식', '간식', '마라탕', '팝콘', '나쵸', '코코팜', '써니텐', '희망', '행복', '100점', '1등', '우승', '파티', '버스킹', '현장 체험 학습', '문주호', '권지용', '제주도', '수학여행', '상점', '배드민턴', '테니스', '낭만', '열정', '솔로', '노래', '아이유', '아이돌', '뉴진스', '롤', '롤체', '발로란트', '발로', '라이엇', '로블록스', '브롤스타즈', '클래시로얄', '컴백', '블랙핑크', '새로운 청바지', '상금', '민지', '하니', '다니엘', '해린', '부자', '돈', '달러', '화폐', '동전', '고양이', '강아지', '만화책', '웹툰', '혜인', '두카미', 'DLC', '스마트팜', '칭찬카드']
bad_word = ['음악', '수업', '강의', '과제', '숙제', '공부', '스페이스', '삼디', 'ALT', '자료구조', '데이터 베이스', 'java', 'js', '돌발', '휴재', 'ppt', '파손', '배열', '집합', '이산수학', '점호', '가창', '회의', '미친', '병신', '냄새', '연애', '커플', '벌점', '코테', '수행', '기말', '중간', '시험', '테스트', '코딩테스트', '오버워치', '국어', '수학', '사회', '과학', '영어', '컴일', '웹기', '미술', '피컴', '악기', '스포츠', '플루트', '플루트 공연', '근', '임규연', '안영세']
hankbok = 0
while True:
    command = input()
    if end(command):
        break
    hankbok = inCheck(command,good_word,bad_word,hankbok)
    print(hankbok)