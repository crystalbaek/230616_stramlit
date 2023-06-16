import streamlit as st

# st. -> ctrl + space -> 다양한 기능(함수, 메소드)을 가지고 있다

st.title("나의 파이썬 웹 페이지")
st.header("수업 8일차에 만들었어요")
st.subheader("그래도 잘 만들었죠?")
st.write("내가 만든 페이지, 너를 위해 구웠지")

st.video("https://www.youtube.com/watch?v=SaCheA6Njc4")
st.image("https://cdn.pixabay.com/photo/2023/06/02/14/12/woman-8035772_1280.jpg")  # 인터넷 링크
st.image("https://i.imgur.com/FD6kOUY.jpeg")
st.image("img/img.jpeg")  # 파일 경로 (app.py)
st.image(image="img/img.jpeg")  # 키워드를 사용해서...
st.image("img/img.jpeg", use_column_width=True)  # 파일 경로 (app.py)
st.image("img/img.jpeg", width=100)  # 파일 경로 (app.py)

# 마크다운
# https://heropy.blog/2017/09/30/markdown/

# st.write / st.markdown
# st.write -> 입력하는 것에 맞춰서 알아서 결정 -> 마크다운
# st.markdown -> 명백하게 마크다운을 실행하겠다

# 제목 마크다운
st.write("""
# 가장 큰 제목  (h1 - headline1 - st.title)
## 그 다음 큰 제목 (h2 - headline2 - st.header)
### 그것보단 작은 제목 <- 대부분 여기까지만 씀 (h3 - headline3 - st.subheader)
#### 좀 더 작은 제목 (h4)
##### 이건 없겠지? (h5)
###### 이것도 있나? (h6)
####### 이건 없어.
""")  # 문자열로 넣으면 마크다운

# 서식
text = """
기울임 : *별표* 또는 _언더바_를 하나씩 써주면
 
진하게(bold) : **별표** 또는 __언더바__를 두개씩 써주면
 
기울임 + 진하게(bold) : ***별표*** 또는 ___언더바___를 세개씩 써주면 

취소선 : ~물결표~

밑줄 : <U>밑줄</u>

형광펜 : <mark>형광펜</mark>

"""

st.write("컴포넌트")
# 위-아래 한 줄로만...

st.write("🤣")
cols = st.columns(2)  # 컬럼 리스트
cols[0].write("🤣")
cols[1].write("🤣")
cols = st.columns(3)

# 🍉 -> n 등분 -> 3등분
cols[0].write("🍉")
cols[1].write("🍉")
cols[-1].write("🍉")
cols = cols[0].columns(3) # 열의 열인 거임
cols[0].write("🍉")
cols[1].write("🍉")
cols[-1].write("🍉")
col1, col2 = st.columns(2)  # 리스트 언패킹
col1.write("왼쪽 열")
col2.write("오른쪽 열")

with col1: # col1을 기준으로 streamli을 써주겠다
    # 블록 (:) 을 열면 -> 이 안에서는 streamlit 기능 실행시 col1에 종속
    st.write("왼쪽")
with col2: # col1을 기준으로 streamli을 써주겠다
    # 블록 (:) 을 열면 -> 이 안에서는 streamlit 기능 실행시 col2에 종속
    st.write("왼쪽")