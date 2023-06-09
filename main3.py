#インタラクティブなウィジット
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image #画像表示のモジュール

#タイトルの追加
st.title('Streamlit 超入門')


#テキスト入力による値の動的変更
st.write('Interactive Widgets')


#2カラムレイアウトにする
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')



# text = st.text_input('あなたの趣味を教えて下さい。')
# condition= st.slider('あなたの今の調子は？', 0, 100, 50) #min,max,初期値

# 'あなたの趣味は、', text
# 'コンディション：', condition

