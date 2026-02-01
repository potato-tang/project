import csv

from utils_C import C  #C모듈 import
from utils_D.internal.core.d_module import D  #D 모듈 import


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


def main():
    print("=== 클래스 import 확인 ===")
    c = C("math")
    c.show()

    d = D(95)
    d.show()

    print("\n=== CSV 경로 읽기 ===") #상대 경로로도 해보고 절대 경로로도 해보기
    path = "data/datasets/exam/scores.csv"
    data1 = read_csv(path)
    print(data1)

    print("\n=== CSV 경로 읽기 ===") #상대 경로로도 해보고 절대 경로로도 해보기
    path = "/Users/woojieun/Downloads/2일차실습/5차시/file_path_example_2_problem/data/datasets/exam/scores.csv"
    data1 = read_csv(path)
    print(data1)

if __name__ == "__main__":
    main()
