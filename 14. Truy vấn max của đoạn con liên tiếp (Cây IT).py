'''
- Đề bài:
Cho dãy số nguyên có n phần tử a1,a2,...,an và m truy vấn mỗi truy vấn có là hai giá trị L,R
cần phải tìm giá trị lớn nhât của dãy con liên tục từ vị trí L đến vị trí R là tìm max của a[L], a[L+1],...,a[R].
- Input:
+) Dòng đầu gồm hai số nguyên dương n và m tương ứng với số phần tử của dãy và số truy vấn
+) Dòng tiếp theo gồm n số nguyên là các phần tử của dãy có giá trị tuyệt đối không vượt quá
+) Các dòng cuối gồm m dòng mỗi dòng chứa hai số dương L,R
- Output:
=> Xuất ra m dòng mỗi dòng là giá trị lớn nhất của dãy con liên tục từ vị trí L đến R

- Ví dụ:
Input:
6 3
4 7 2 8 1 -6
1 5
2 3
3 6
Output:
8
7
8
'''

'''
1. Ý tưởng thuật toán
- Xây dựng cây Segment Tree với mỗi node biểu diễn một đoạn của dãy số ban đầu.
- Mỗi node trong cây Segment Tree sẽ lưu giá trị lớn nhất của dãy con liên tục từ vị trí L đến R của đoạn tương ứng.
- Để cập nhật giá trị của một phần tử trong dãy ban đầu, ta sẽ cập nhật giá trị tại node phù hợp trong cây Segment Tree.
- Để truy vấn giá trị lớn nhất từ vị trí L đến R, ta sẽ thực hiện truy vấn trên cây Segment Tree.
2. Các bước triển khai
B1: Tạo cây IT với các node 
    +) Cây trái, cây phải
    +) elem = -1e^9
    +) Cây con trái, cây con phải
B2: Duyệt i-> n cập nhập cây bằng cách
    - Nếu a > gốc -> elem = ai
    - Tùy theo vị trí của i đi xuống nút lá
B3: Truy vấn
    - Nếu ở 1 bên -> tìm 1 bên
    - Nếu ở 2 bên, tìm cả 2 bên so sánh với nhau
'''



