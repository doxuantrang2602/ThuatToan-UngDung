'''
- Đề bài:
    Cho dãy n phần tử a1,a2,...,an
    Tìm một dãy con liên tục nhiều phần tử nhất có thể sao cho trong dãy con đó không có bất kỳ 2 phần tử nào bằng nhau
- Input:
+) Dòng đầu gồm n là số phần tử của dãy (1<=n<=1000)
+) Dòng cuối chứa n số nguyên không âm có giá trị không vượt quá 32767
- Output:
+) Một số tự nhiên duy nhất là độ dài của dãy con liên tục dài nhất thoải mãn không có cặp 2 phần tử bất kỳ nào bằng nhau

- Ví dụ:
Input
12
4 7 2 8 4 8 3 2 4 9 3 6
Output
5
*Giải thích có hai dãy con liên tục có 5 số liên tiếp thỏa mãn như 8,3,2,4,9 hoặc 2,4,9,3,6
'''

'''
1. Ý tưởng thuật toán:
- Sử dụng một danh sách (list) để lưu trữ dãy số nguyên đầu vào.
- Sử dụng một biến res để lưu kết quả tạm thời (độ dài của dãy con liên tục dài nhất không có cặp 2 phần tử bất kỳ nào bằng nhau).
- Sử dụng một biến p để lưu vị trí bắt đầu của dãy con liên tục hiện tại.
- Sử dụng một từ điển (dictionary) D để lưu vị trí xuất hiện gần nhất của từng phần tử trong dãy.
2.Các Bước Triển Khai:
B1: Đọc số nguyên n từ input, đại diện cho số phần tử của dãy.
B2: Đọc dãy số nguyên a từ input và lưu vào danh sách a.
B3: Khởi tạo biến res và p bằng 0.
B4: Khởi tạo từ điển D để lưu vị trí xuất hiện của các phần tử.
B5: Duyệt qua từng phần tử x và vị trí i tương ứng trong dãy a:
- Nếu x đã xuất hiện trước đó và vị trí xuất hiện gần nhất của x (D[x]) lớn hơn hoặc bằng p
    => p = D[x] + 1
- res = max(res, i - p + 1)
- Cập nhật vị trí xuất hiện của x trong từ điển D thành i.
B6: print(res)
'''
if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    res = 0
    p = 0
    D = {}
    for i,x in enumerate(a):
        if x in D and D[x]>=p:
            p = D[x]+1
        res = max(res, i-p+1)
        D[x] = i
    print(res)


