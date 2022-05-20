import streamlit as st
import pandas as pd
import seaborn as sb

def run_eda() :
    st.subheader('데이터 분석')

    car_df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Car_Purchasing_Data.csv', encoding='ISO-8859-1')

    # 라디오버튼을 이용해서, 데이터프레임과, 통계치를 선택해서 보여줄수 있도록 만든다.

    radio_menu = ['데이터프레임', '통계치']
    selected = st.radio('선택하세요', radio_menu)

    if selected == radio_menu[0] :
        st.dataframe( car_df )
    elif selected == radio_menu[1] :
        st.dataframe(car_df.describe())