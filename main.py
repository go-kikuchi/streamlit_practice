import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image #画像表示のモジュール

#タイトルの追加
st.title('Streamlit 超入門')

#テキストの追加
st.write('DataFrame')

#表データの追加
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

#表の表示
st.write(df)
st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
"""
dataframeは表の細かい設定ができる
axis=0:縦 axis=1:横
hilight_maxで最大にフォーカス
"""
st.table(df)
"""
tableは静的な表を表示
dataframeは動的な表を表示
"""


#マジックコマンドの使用
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a','b','c']
)

#チャートを描く
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)



#マップをプロット
df = pd.DataFrame(
    np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)


#画像を表示
st.write('Display Image')

img = Image.open('sample.jpg')
st.image(img, caption='愛しきハナちゃん', use_column_width=True)

