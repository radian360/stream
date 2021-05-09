import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Hello')
st.write('Interactive Widge')

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)

'あなたが好きな数字は', option, 'です。'
# if st.checkbox('Show Image'):
#     img = Image.open('IMG_4052.jpg')
#     st.image(img, caption='小槌', use_column_width=True)


 

