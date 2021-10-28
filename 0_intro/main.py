import time

import streamlit as st
# import numpy as np
# import pandas as pd
# import plotly.express as px
# from PIL import Image

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)


text = st.text_input('あなたの趣味を教えて下さい。')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味：', text
'コンディション：', condition

# if st.checkbox('Show Image'):
#     img = Image.open('alpha_stmoritz_train.jpg')
#     st.image(img, caption='train', use_column_width=True)

# option = st.selectbox(
#     'あなたが好きな数字を教えてください、',
#     list(range(1,11))
# )

# 'あなたの好きな数字は、', option, 'です。'

# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# #st.table(df.style.highlight_max(axis=0))
# st.map(df)



#df = [dict(Occupier="A", Start="2009-01-01", Finish="2009-02-28", Room="201"),
#      dict(Occupier="C", Start="2009-02-20", Finish="2009-05-30", Room="202"),
#      dict(Occupier="B", Start="2009-03-05", Finish="2009-04-15", Room="201"),
#      dict(Occupier="D", Start="2009-03-20", Finish="2009-05-30", Room="101")
#      ]
#fig = px.timeline(df, x_start="Start", x_end="Finish", y="Room", color="Room")

#st.plotly_chart(fig)

