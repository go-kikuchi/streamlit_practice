#インタラクティブなウィジット
import streamlit as st
import time

st.title('Streamlit 超入門')

#プログレスバーの表示
st.write('プログレスバーの表示')
'Start!!'

latest_literation =st.empty() #空の要素
bar = st.progress(0)

for i in range(100):
    latest_literation.text(f'Iteration{i+1}') #テキストの表示
    bar.progress(i + 1) #バーの表示
    time.sleep(0.01) #タイムの速さ指定


'Done!!'

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

