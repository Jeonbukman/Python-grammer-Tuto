#문자열 포맷
# print("a"+"b")
# print("a","b")

# 기호 사용하지 않고 포맷하는 법
# 방법 1
# print("나는 %d살입니다" % 20) # 'd'는 정수값만 대입
# print("나는 %s을 좋아해요." %"파이썬") #'s'는 스트링 =문자열
# print("Apple은 %c로 시작해요." %"A") # %c는 캐릭터, 한글자만 받음
# %s로만 해도 됨
# print("나는 %s살입니다" %20)
# print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

# 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))

# 방법 4 (py v3.6이상부터)
# age =20
# color ="빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")


#탈출문자
# \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타") 

# 저는 "학생"입니다. 라고 적고싶다
# \" , \' : 문장 내에서 따옴표 역할
# print("저는 '학생'입니다.") 
# print('저는 "학생"입니다.')
# print("저는 \"학생\"입니다.")
# print("저는 \'학생\'입니다.")

# \\ : 문장 내에서 \ 역할
# print("C:\\Users\\kimse\\Desktop\\Pythonworkspace>")

# \r  커서를 맨 앞으로 이동
# print("Red apple\rPine") # Pineapple

# \b : 백스페이스 역할
# print("Red\bApple") # ReApple

# \t : 탭 (4칸씩 이동/ 스페이스바 느낌)
# print("Red\tApple") # Red    Apple