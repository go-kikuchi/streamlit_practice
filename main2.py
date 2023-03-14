#インタラクティブなウィジット
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image #画像表示のモジュール

#タイトルの追加
st.title('Streamlit 超入門')

#チェックボックスによるメディアの表示可否
st.write('Display Image')

if st.checkbox('Show Image'): #Trueを返す,if文が重要
    img = Image.open('sample.jpg')
    st.image(img, caption='愛しきハナちゃん', use_column_width=True)

#セレクトボックスによる値の動的変更
st.write('Display Image')

option = st.selectbox(
    'あなたが好きな数字を教えて下さい。',
    list(range(1,11))
    )
'あなたの好きな数字は、', option, 'です。'


#テキスト入力による値の動的変更
st.write('Interactive Widgets')

text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味は、', text, 'です。'

#スライダーによる動的変更
condition= st.slider('あなたの今の調子は？', 0, 100, 50) #min,max,初期値
'コンディション：', condition