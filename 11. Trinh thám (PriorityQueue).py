'''
- Đề bài:
Amas là một sinh viên mới vào học tại ĐHGVTVT năm thứ nhất. Kết thúc học kỳ 1, Amas được tham gia một học kỳ quân sự.
Hôm nay, lớp học của Amas được chia làm 2 phía chiến trường và tổ chức tập trận, Amas tham gia bên phía quân xanh có
nhiệm vụ đi trinh thám quân đỏ huấn luyện. Amas leo lên một quả đồi và sử dụng ống nhòm để quan sát thì phát hiện ra
quân đỏ đang dàn hàng ngang để tập luyện, khổ nỗi ống nhòm nhỏ nên mỗi khung nhìn chỉ quan sát được một số lính liên
tiếp của quân đỏ. Nhiệm vụ trinh thám lần này là tìm ra chiều cao cao nhất của đối phương, để làm được điều đó rất khó
nên phải quan sát dần dần lần lượt từ đầu đến cuối của hàng bằng cách dịch khung nhìn lần lượt mỗi lần tịnh tiến lên một đơn vị.
* Bài toán đặt ra với Amas là với n quân đỏ có chiều lượt là a1,a2,...,an, khung nhìn có khoảng rộng là 1<=k<=n.
  Khi dịch khung nhìn lần lượt từ đầu đến cuối thì với từng vị trí khung nhìn phải tìm ra chiều cao của quân đỏ
  cao nhất trong khung nhìn đó
- Input:
+) Dòng đầu chứa 2 số n là số quân đỏ (1<=n<=10^5) và k là khung nhìn của ống nhòm (1<=k<=n)
   (số quân đỏ tối đa mà một lần ống nhòm quan sát được)
+) Dòng thứ 2 chứa n số nguyên là chiều cao của quân đỏ theo đơn vị chiều cao (1<=ai<=10^4)
- Output:
=> Kết quả đầu ra gồm n-k+1 số nguyên là chiều cao của quân đỏ cao nhất trong từng khung nhìn

- Ví dụ:
Input:
8 3
4 7 2 5 6 3 9 1
Output:
7 7 6 6 9 9
* Giải thích:
- Lần lượt khung nhìn duyệt qua 3 phần tử một tìm max(4,7,2),max(7,2,5),max(2,5,6),max(5,6,3),max(6,3,9),max(3,9,1)
'''

'''
1. Ý tưởng
- Sử dụng hàng đợi ưu tiên lớn mỗi phần tử (chiều cao và vị trí)
2. Triển khai thuật toán
B1: Khởi tạo PQ 
B2: Nhập n, k, a1,a2,...,an
B3: Duyệt chiều cao x có vị trí i từ 1 đến n
    - Thêm (chiều cao, vị trí) vào PQ: PQ.put([-x,i])
    - Nếu i>=k:
        +) Lấy ra những phần tử đứng đầu mà nằm ngoài khoảng k đang xét
        +) In ra phần tử x đứng đầu PQ: PQ.queue[0][0]
'''
import queue
if __name__ == "__main__":
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    PQ = queue.PriorityQueue()
    for i,x in enumerate(a,1):
        PQ.put([-x,i])
        if i>=k:
            while PQ.qsize()>0 and PQ.queue[0][1] < i-k+1:
                PQ.get(x)
            print(-PQ.queue[0][0], end=" ")

