'''
- Đề bài:
Toto nhận được nhiệm vụ trông nom bò sữa nhà mình đang ăn cỏ trên cánh đồng.
Giả sử cánh đồng là một lưới tọa độ, các con bò đang ở các tọa độ nguyên trên cánh đồng đó và Toto thì đang ở gốc tọa độ.
Nếu hai con bò bất kỳ mà thằng hàng (hoặc trùng nhau) cùng phía so với Toto thì Toto chỉ nhìn thấy con ở phía trước
mà không nhìn thấy con ở phía sau bị che lấp.
Giả sử mắt của Toto rất tốt nếu không có vật cản thì con bò ở xa mấy cũng nhìn thấy.
- Input:
+) Dòng đầu là số con bò là một số nguyên dương n (1<=n<=10^5)
+) Các dòng tiếp theo gồm n dòng mỗi dòng có hai giá trị x[i],y[i] không có trùng với gố tọa độ,
   có giá trị tuyệt đối không vượt quá 1000, tương ứng với tọa độ của con bò thứ i
- Output:
=> Số con bò mà Toto nhìn thấy
- Ví dụ:
Input
6
3 3
7 7
4 6
-1 -1
6 9
3 3
Output
3
*Giải thích:
Toto nhình thấy các con bò ở vị trí (3,3); (4,6) và (-1,-1)
Con bò ở vị tọa độ (7,7) và (3,3) bị con bò ở tọa độ (3,3) che khuất
Con bò ở vị tọa độ (6,9) bị con bò ở tọa độ (4,9) che khuất
'''

'''
1. Ý tưởng thuật toán:
- Thuật toán sử dụng ý tưởng của chuẩn hóa hướng từ Toto đến mỗi con bò dựa trên ước số chung lớn nhất (gcd)
  của tọa độ x và y. 
- Mục tiêu là để xác định các hướng duy nhất mà Toto có thể nhìn thấy con bò, với giả định rằng con bò ở xa 
  nhưng nằm trên cùng một hướng sẽ bị che khuất bởi con bò gần hơn.
2. Các Bước Triển Khai:
B1: Nhập số lượng con bò n và tọa độ của từng con bò.
B2: Khởi tạo danh sách a để lưu trữ các hướng tối giản từ Toto đến mỗi con bò.
B3: Duyệt qua từng con bò, tính gcd của tọa độ x và y, sau đó chuẩn hóa tọa độ bằng cách chia chúng cho gcd. 
    Thêm hướng tối giản vào danh sách a.
B4: Sử dụng Counter để đếm số lần xuất hiện của mỗi hướng tối giản trong danh sách.
B5: In ra số lượng hướng duy nhất trong Counter, tương ứng với số lượng con bò mà Toto có thể nhìn thấy.
'''

import math
if __name__ == "__main__":
    n = int(input())
    s = set()
    for i in range(n):
        x, y = map(int,input().split())
        d = math.gcd(x,y)
        x //= d
        y //= d
        s.add((x,y))
    print(len(s))


