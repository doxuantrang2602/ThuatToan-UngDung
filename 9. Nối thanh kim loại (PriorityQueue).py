'''
- Đề bài:
Công việc cơ khí thật là mệt nhọc, muốn nối một thanh kim loại độ dài a với một thanh kim loại độ dài b
thì kinh phí để thuê nối tốn mất a+b đơn vị tiền tệ. Hiện nay Tichpx cần nối n thanh kim loại lần lượt
có độ dài là a1,a2,...,an thành một đoạn theo bạn Tichpx nên bố trí thế nào để tổng số tiền phải trả
là ít nhất.
- Input:
+) Dòng đầu chứa số nguyên dương n (1<=n<=10^5)
+) Dòng tiếp theo là n số nguyên dương tương ứng là độ dài các thanh muốn nối (1<=ai<=10^3)
- Output:
=> Một số nguyên dương là số kinh phí ít nhất phải trả

- Ví dụ:
Input
3
8 4 6
Output
28
* Giải thích :
- Nếu ta nối thanh 8 với thanh 4 tốn chi phí là 8+4=12 sau khi nối xong còn 2 thanh độ dài 12 và 6 nối lại với nhau
  tốn 12+6=18 tổng chi phí nối là 12+18=30.
- Nếu ta nối 4 với 6 trước tốn 10 và còn 2 thanh 10 và 8 nối lại với nhau tốn 18 do đó tổng kinh phí ít hơn chỉ còn 28
'''
import queue

'''
1. Ý tưởng thuật toán
- Sử dụng hàng đợi ưu tiên để luôn lấy ra các thanh kim loại có độ dài ngắn nhất trước.
- Lặp qua từng bước, lấy ra hai thanh kim loại ngắn nhất, nối chúng lại với nhau và đưa vào hàng đợi.
- Lặp cho đến khi chỉ còn một thanh kim loại trong hàng đợi, tức là đã nối được tất cả các thanh thành một đoạn.
2. Các bước triển khai 
B1: Nhập n và a1,a2,...
B2: Khởi tạo PriorityQueue, res = 0 để lưu kết quả
B3: Thêm a1,a2,... vào hàng đợi
B4: Duyệt Q.qsize()>1:
    - Lấy ra 2 thanh nhỏ nhất:x = Q.get() + Q.get()
    - Cập nhật res += x
    - Thêm thanh mới vào hàng đợi: Q.put(x)
B5: In ra res
'''

if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    Q = queue.PriorityQueue()
    res = 0
    for x in a:
        Q.put(x)
    while Q.qsize()>1:
        x = Q.get()+Q.get()
        res += x
        Q.put(x)
    print(res)