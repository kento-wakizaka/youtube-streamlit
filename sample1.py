#選択した範囲で「 ctrl + / 」で全部コメントアウト

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit入門') #タイトルの表示

# st.write('DataFrame') #テキストの表示
st.write('Interactive Widget')

################################################ checkbox ################################################
if st.checkbox('Show Image'): #画像が表示された際に画像を表示させるように制御
    image = Image.open('sora_.JPG') #変数に画像データを格納
    st.image(image,caption='sora',use_column_width=True) #画像の表示
##########################################################################################################

################################################# selectbox ##############################################
option1 = st.selectbox('あなたの好きな数字を教えてください。',list(range(1,11)))
'あなたの好きな数字は',option1,'です。'
##########################################################################################################

################################################ text_input ##############################################
text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味:',text
##########################################################################################################

################################################## slider ################################################
condition = st.slider('あなたの今の調子は',0,100,50) #sliderの表示 (表示文字,最小値,最大値,初期値)
'あなたの調子:',condition
##########################################################################################################

# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40]
# })

#ランダムな値を入力した3x20の表
# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns = ['a','b','c']
# )

#緯度経度にランダムな値を50で割った値に[35.69,139.70]を加算した値を入力した2x100の表(新宿付近の座標をランダムで表示する)

# st.write(df) #dfの表を表示する

#st.dataframe(df,width=100,height=100) #同じく表を表示するが、立幅と横幅を指定できる

#st.dataframe(df.style.highlight_max(axis=0)) #一番大きい値に色付けする axis...軸

#st.table(df.style.highlight_max(axis=0)) #静的なテーブルの表示 ソートとかがない

# st.line_chart(df) #dfの表を折れ線グラフで表示

# st.area_chart(df) #dfの表を折れエリアを囲んだ図をで表示

# st.bar_chart(df) #dfの表を棒グラフで表示

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

