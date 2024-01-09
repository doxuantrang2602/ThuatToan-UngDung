'''
- Đề bài:
Một bàn cờ vua có kích thước 1000x1000, các hàng được đánh số từ 1 đến 1000 lần lượt từ trên xuống dưới,
các cột được đánh số từ 1 đến 1000 lần lượt từ trái sang phải, quân tượng là quân có thể di chuyển theo
đường chéo và ăn các quân cờ khác. Giả sử trên bàn cờ có n quân tượng, nhiệm vụ của bạn là hãy đếm số
quân tượng có thể ăn nhau trên bàn cờ
(Hai quân tượng có thể ăn nhau kể cả giữa chúng có một quân tượng khác).
- Input:
+) Dòng đầu tiên chứa số nguyên n là số quân tượng
+) N dòng tiếp theo, mỗi dòng chứa hai số xi và yi là tọa độ của quân tượng thứ i trên bàn cờ.
- Output:
=> Số quân tượng có thể ăn nhau trên bàn cờ.

- Ví dụ:
Input
3
1 1
5 5
9 9
Output
3
'''
'''
1. Ý tưởng thuật toán:
- Thuật toán dựa trên việc sử dụng hai bộ đếm (Counter) để theo dõi số lượng quân tượng 
  trên mỗi đường chéo chính và phụ của bàn cờ. 
- Quân tượng trên cùng một đường chéo có thể "ăn" lẫn nhau. 
- Đường chéo chính được xác định bởi giá trị x - y, trong khi đường chéo phụ được xác định bởi x + y. 
  Từ đó, thuật toán đếm số cặp quân tượng có thể ăn nhau trên mỗi đường chéo.
2. Các Bước Triển Khai:
B1: Nhập n quân tượng và tọa độ của từng quân tượng.
B2: Sử dụng Counter để đếm số lượng quân tượng trên mỗi đường chéo chính (dựa trên x - y) 
    và mỗi đường chéo phụ (dựa trên x + y).
B3: Khởi tạo res = 0 để tính tổng số cặp quân tượng có thể ăn nhau trên mỗi đường chéo. 
    Đối với mỗi đường chéo, số cặp quân tượng có thể ăn nhau là res+=y*(y-1)/2 
B4: Cộng tổng số cặp trên tất cả các đường chéo chính và phụ để nhận kết quả cuối cùng.
'''
from collections import Counter
if __name__ == "__main__":
    n = int(input())
    A = []
    for i in range(n):
        x,y = map(int,input().split())
        A.append([x,y])
    C = Counter(x[0]-x[1] for x in A) # Đường chéo chính
    P = Counter(x[0]+x[1] for x in A) # Đường chéo phụ
    res = 0
    for x,y in C.items():
        res += y*(y-1)//2
    for x,y in P.items():
        res += y*(y-1)//2
    print(res)



