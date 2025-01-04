import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the processed data
file_path = 'flu_data_processed.csv'
flu_data = pd.read_csv(file_path, encoding='utf-8-sig')

# Streamlit app
st.title("연도별 Flu 감염 현황")
st.write("연도별 주차에 따른 Flu 감염 데이터를 시각화합니다.")

# Select a year
years = flu_data["year"].unique()
selected_year = st.selectbox("연도를 선택하세요", years)

# Filter data for the selected year
year_data = flu_data[flu_data["year"] == selected_year].iloc[0, 1:]
weeks = year_data.index
values = year_data.values

# Identify the week with a sharp increase
sharp_increase_week = None
for i in range(2, len(values)):
    if values[i] > values[i-1] * 1.5:  # Detect a 50% increase
        sharp_increase_week = weeks[i-2]  # Recommend 2 weeks before the sharp increase
        break

# Display vaccination recommendation
if sharp_increase_week:
    st.write(f"⚠️ 예방 접종 권장: {sharp_increase_week} 주에 독감 예방 백신을 맞으세요.")

# Plot the line chart
st.subheader(f"{selected_year} Flu 감염 추이")
plt.figure(figsize=(10, 6))
plt.plot(weeks, values, marker='o')
plt.title(f"{selected_year} Flu 감염 추이")
plt.xlabel("주")
plt.ylabel("감염 수")
plt.xticks(rotation=45)
plt.grid()
st.pyplot(plt)
