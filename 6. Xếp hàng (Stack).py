'''
- Đề bài:
Toto chuẩn bị thi môn Phân Tích Thiết Kế Thuật toán nên ôn ngày ôn đêm, mệt quá thiếp đi trên bàn phím và bị xuyên không về thế kỷ XVIII
vào ngay Quốc Tử Giám gặp bao nhiêu là sỹ tử đang xếp hàng chuẩn bị thi môn "Đại thành toán pháp". Quan Chánh chủ khảo là cụ Lê Quý Đôn
đang gọi thí sinh vào phòng thi trông thấy Toto liền ra bài toán như sau:
* Hãy đếm xem trong dãy các sĩ tử đang xếp thành một hàng dài thẳng tắp có bao nhiêu cặp hai người nhìn thấy nhau,
  tức là giữa hai người không có ai cao hơn một trong hai người đó.
Toto muốn quay về đi thi nhưng cụ tránh chủ khảo nói là phải trả lời được mới cho về. Bạn hãy giúp Toto nhé
- Input:
+) Dòng đầu chứa số nguyên dương n là số người đang xếp hàng (1<=n<=10^5)
+) Dòng thứ 2 là chiều cao của các sĩ tử theo đơn vị thời đó là số nguyên dương có giá trị không vượt quá 10^9
- Output:
=> Một số tự nhiên là kết quả bài toán

- Ví dụ 1:
Input
6
7 6 5 1 4 2
Output
6

- Ví dụ 2:
Input
8
4 7 2 8 4 4 4 6
Output
14

* Giải thích Ví dụ 2:
Để dễ đếm cặp ta chỉ xét người trước nhìn về phía sau:
Người thứ nhất có chiều cao 4 nên chỉ nhìn thấy 1 người thứ 2
Người thứ hai có chiều cao 7 nên nhìn thấy 2 người thứ 3, thứ 4
Người thứ ba chiều cao 2 nên chỉ nhìn thấy 1 người thứ 4
Người thứ tư chiều cao 8 nên chỉ nhìn thấy 4 người thứ 5, thứ 6, thứ 7, thứ 8
Người thứ năm chiều cao 4 nên chỉ nhìn thấy 3 người thứ 6, thứ 7, thứ 8
Người thứ sáu chiều cao 4 nên chỉ nhìn thấy 2 người thứ 7, thứ 8
Người thứ bảy chiều cao 4 nên chỉ nhìn thấy 1 người thứ 8
Người thứ tám không còn ai
'''
'''
1. Ý tưởng thuật toán
- Sử dụng một hàng đợi LIFO (Last In First Out) để lưu trữ chiều cao của các sĩ tử 
  và số lượng cặp nhìn thấy được tạo ra bởi mỗi sĩ tử.
- Duyệt qua từng sĩ tử trong hàng, loại bỏ những sĩ tử có chiều cao thấp hơn từ hàng đợi 
  và cộng dồn số lượng cặp nhìn thấy vào tổng kết quả (res).
- Khi gặp sĩ tử có chiều cao bằng với chiều cao trên cùng của hàng đợi
  => Cập nhật số lượng cặp nhìn thấy và tiếp tục quá trình.
2. Triển khai thuật toán
B1: Nhập n, a1,...,an
B2: S = rỗng
B3: res=0
B4: Duyệt x trên a1,...,an
- Lấy hết các phần tử (nếu có) < x: 
  => Cộng tần suất của những phần tử < x
- Khởi tạo S cùng tần suất vào res
- Nếu S.top() = x thì 
    +) res tăng tần suất của top và tăng lên 1 nếu S.size() >=2
    +) tần xuất S.top() tăng lên 1
- Ngược lại :
    +) res tăng lên 1 nếu S.size() > 0
    +) S.push([x,1])
B5: Xuất res
'''
import queue
if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    s = queue.LifoQueue()
    res = 0
    for x in a:
        while s.qsize()>0 and s.queue[-1][0] < x:
            res += s.get()[1]
        if s.qsize()>0 and s.queue[-1][0] == x:
            u = s.get()[1]
        else:
            u = 0
        res += u + (s.qsize()>0)
        s.put([x,u+1])
    print(res)

