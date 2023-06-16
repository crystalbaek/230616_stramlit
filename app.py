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