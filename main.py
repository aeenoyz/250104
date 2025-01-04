import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 감기 환자 수 데이터 생성
np.random.seed(42)
dates = pd.date_range(start="2024-01-01", end="2024-01-31")
cold_cases = np.random.randint(50, 200, size=len(dates))
data = pd.DataFrame({"Date": dates, "Cold Cases": cold_cases})

# 페이지 설정
st.set_page_config(page_title="Cold Cases Visualization", layout="wide")

# 제목
st.title("Daily Cold Cases Visualization")

# 그래프 생성
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data["Date"], data["Cold Cases"], marker='o', linestyle='-', linewidth=2)
ax.set_title("Daily Changes in Cold Cases", fontsize=16)
ax.set_xlabel("Date", fontsize=14)
ax.set_ylabel("Number of Cases", fontsize=14)
plt.xticks(rotation=45)

# 마우스 오버와 유사한 데이터 표시
hover_data = st.selectbox("Select a date to view details:", data["Date"].dt.strftime('%Y-%m-%d'))
selected_data = data[data["Date"].dt.strftime('%Y-%m-%d') == hover_data]

st.write(f"**Date**: {selected_data.iloc[0]['Date'].strftime('%Y-%m-%d')}  ")
st.write(f"**Cold Cases**: {selected_data.iloc[0]['Cold Cases']}")

# 그래프 표시
st.pyplot(fig)

# 데이터 표시 옵션
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.dataframe(data)
