# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수+ "!"로 구성
#               (nav)                 (5)             (1)       (!)
# 예) 생성된 비밀번호 : nav51!

# url = "https://naver.com"

# A = url.replace("https://", "") #제외할 부분을 리플로써 빈칸으로.
# A = A[:A.index(".")] # A 의 처음부터 A의 .이 위치하기 전까지
# password = A[:3] + str(len(A)) + str(A.count("e")) + "!"
# print("{0} 의 비밀번호는 {1}입니다.".format(url, password))

