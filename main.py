import streamlit as st

import pandas as pd
import numpy as np
import plotly.express as px

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
fig = px.line(data, x="Date", y="Cold Cases", title="Daily Changes in Cold Cases", 
              labels={"Date": "Date", "Cold Cases": "Number of Cases"},
              hover_data={"Cold Cases": True, "Date": False})

# 그래프 스타일
fig.update_traces(line=dict(width=3))
fig.update_layout(
    hovermode="x unified",
    template="plotly_white",
    title_font_size=24,
    xaxis_title_font_size=18,
    yaxis_title_font_size=18
)

# 그래프 표시
st.plotly_chart(fig, use_container_width=True)

# 데이터 표시 옵션
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.dataframe(data)
