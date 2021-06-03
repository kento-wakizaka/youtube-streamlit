import streamlit as st
import time

########################## column ##########################

# プログレスバーを0.1sごとに増やしていく。それ以降の処理は待たされる。
latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Interation {i+1}%')
    bar.progress(i+1)
    time.sleep(0.01)

#############################################################


########################## column ##########################

# 右カラムと左カラムを定義してるっぽい
left_column,right_column = st.beta_columns(2)

# ボタンを押したら右カラムに「ここは右カラム」という文字列を表示
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

#############################################################


########################## sidebar ##########################

#「st.sidebar.なんか」でサイドバーにおける。
hobby = st.sidebar.text_input('あなたの趣味を教えてください')
st.sidebar.write('あなたの趣味：',hobby)

#############################################################


########################## expander ##########################

# +を押すと問い合わせの内容を表示する。
expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の内容')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の内容')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3の内容')

##############################################################

#


# ctrl+Dで同じの全て選択できるので、一括で消したり名前の変更ができる。