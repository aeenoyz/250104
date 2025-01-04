import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
file_path = 'pertussis.csv'
data = pd.read_csv(file_path, encoding='euc-kr')

# 열 이름 정리 (공백 제거 및 확인)
data.columns = data.columns.str.strip()
weeks = [f"{week}주" for week in range(1, 53)]

# 열 이름이 예상과 같은지 확인
missing_weeks = [week for week in weeks if week not in data.columns]
if missing_weeks:
    print(f"다음 열이 데이터프레임에 없습니다: {missing_weeks}")
    available_columns = ', '.join(data.columns)
    print(f"사용 가능한 열: {available_columns}")
    raise ValueError("열 이름 불일치로 인해 실행이 중단되었습니다.")

# 1주부터 52주 데이터만 추출
region_data = data.set_index('지역')[weeks]

# 그래프 생성
plt.figure(figsize=(12, 8))
for region in region_data.index:
    plt.plot(weeks, region_data.loc[region], marker='o', label=region)

# 그래프 스타일 설정
plt.title('지역별 1주~52주 백일해 통계', fontsize=16)
plt.xlabel('주', fontsize=14)
plt.ylabel('발생 건수', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='지역', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# 그래프 출력
plt.show()
