import streamlit as st
import numpy as np
import pandas as pd

st.title('Hello')
st.write('DataFrame')


#st.latex(r'''
#    \frac{1}{2}+\frac{1}{3}=\frac{1}{6}
#''')


df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns= ['lat', 'lon']
)

#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
st.map(df)


