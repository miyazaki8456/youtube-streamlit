import streamlit as st

import time

st.title('Streamlit 超入門')
st.write('プログレスバーの表示')
'Start!!'


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)
    
'Done!!!!!'
    






left_column, right_column = st.columns(2)
button = left_column.button('右カラムにボタンを表示')
if button:
    right_column.write('ここは右カラム')
    
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
# text = st.text_input('穴たんお趣味を教えてください。')
# 'あなたの趣味：',text

# condition = st.slider('あなたの今の調子は？',0, 100, 50)
# 'Condition:', condition               
# st.write('DataFrame')
# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、',option,'です。'


# if st.checkbox('Show Image'):
#     img = Image.open('TurnsBeat.jpg')
#     st.image(img, caption='TurnsBeat', use_column_width=True)

audio_file = open('TurnsBeat.wav', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/wav')
# 棒グラフ
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
# st.bar_chart(df)

# テーブル表
# st.table(df.style.highlight_max(axis=0))





# マークダウン記法

# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# マップ
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)