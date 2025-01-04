import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the data
file_path = 'pertussis.csv'
column_names = ["지역", "전체"] + [f"{i}주" for i in range(1, 52)]
pertussis_data = pd.read_csv(file_path, encoding='ISO-8859-1')
pertussis_data.columns = column_names
pertussis_data["지역"] = pertussis_data["지역"].apply(lambda x: x.encode('ISO-8859-1').decode('euc-kr'))

# Streamlit app
st.title("백일해 데이터 분석")
st.write("주별 및 지역별 백일해 사례를 분석하는 대시보드입니다.")

# Select region
regions = pertussis_data["지역"].unique()
selected_region = st.selectbox("지역 선택", regions)

# Filter data for the selected region
region_data = pertussis_data[pertussis_data["지역"] == selected_region]
weeks = [f"{i}주" for i in range(1, 52)]

# Plot weekly trend for the selected region
st.subheader(f"{selected_region}의 주별 백일해 사례 수")
plt.figure(figsize=(10, 6))
plt.plot(weeks, region_data.iloc[0, 2:].values, marker='o')
plt.title(f"{selected_region}의 주별 백일해 사례 추이")
plt.xlabel("주")
plt.ylabel("사례 수")
plt.xticks(rotation=45)
st.pyplot(plt)

# Plot trends for all regions
st.subheader("모든 지역의 주별 사례 수 비교")
plt.figure(figsize=(12, 8))
for _, row in pertussis_data.iterrows():
    plt.plot(weeks, row[2:].values, marker='o', label=row["지역"])
plt.title("지역별 주별 백일해 사례 추이")
plt.xlabel("주")
plt.ylabel("사례 수")
plt.xticks(rotation=45)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
st.pyplot(plt)
