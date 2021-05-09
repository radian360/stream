import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Hello')
st.write('プレグレスバー')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)



left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラム')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ1')
expander.write('問い合わせ1の内容を書く')
expander = st.beta_expander('問い合わせ2')
expander.write('問い合わせ2の内容を書く')
expander = st.beta_expander('問い合わせ3')
expander.write('問い合わせ3の内容を書く')

# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# cod = st.slider('あなたの今の調子は？',0 , 100, 50)

#'あなたの趣味は', text, 'です。'
#'コンディション：', cod
# if st.checkbox('Show Image'):
#     img = Image.open('IMG_4052.jpg')
#     st.image(img, caption='小槌', use_column_width=True)


 

