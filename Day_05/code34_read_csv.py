# 공공데이터포털 CSV파일 읽기
# 부산광역시 시내버스, 마을버스 현황
import csv


fileName = 'busanbus.csv'
dirName = 'C:/Source/studypython2023/'
# 주소 마지막에 구분자를 써주는게 좋음 
fullPath = dirName + fileName


file = open(fullPath, 'r', encoding='utf-8')
reader = csv.reader(file, delimiter=',')
# delimiter = 구분자,
next(reader)
# 리스트 형태로 한 줄 씩 불러옴

for line in reader:
    print(line)

file.close()    # 반드시 닫아야함