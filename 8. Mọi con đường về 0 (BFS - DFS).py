'''
- Đề bài:
Số nguyên dương n nếu phân tích thành tích hai số tự nhiên a*b (a<=b) thì nó sẽ sinh ra số tự nhiên m = (a-1)*(b+1)
cứ tiếp tục như vậy nếu m>0 nó tiếp tục sinh ra số tiếp theo.
Bài toán đặt ra cho số n nguyên dương nó sẽ sinh ra các con và các con lại tiếp tục sinh ra các cháu ... cứ như vậy
tới khi sinh ra tới các số 0 thì sẽ tạo thành một cây.
Nam đang học thuật toán duyệt DFS và BFS để tìm ra tất cả các số mà sinh ra bởi số n cho trước nhưng chưa biết cài đặt
như thế nào bạn hãy giúp Nam nhé
- Input:
+) Một số tự nhiên n
- Output:
=> Liệt kê các giá trị sinh ra được từ n theo thứ tự tăng dần

- Ví dụ 1:
Input
12
Output
0 3 4 6 7 10 12

- Ví dụ 2:
Input
18
Output
0 3 4 5 6 8 10 14 18
'''
import queue

'''
Thuật toán BFS và DFS
VD: Bài toán mọi con đường về 0
Cho n=a*b (a<=b) m =(a-1)(b+1)
1. Ý tưởng
- Sử dụng thuật toán DFS hoặc BFS để duyệt qua các số sinh ra từ số n theo quy tắc đã cho.
- Sử dụng cấu trúc dữ liệu stack để lưu trữ các số cần duyệt.
- Dùng một tập hợp (set) để kiểm tra số đã xuất hiện hay chưa và tránh lặp lại.
2. Triển khai thuật toán
B1: Nhập n
    Khai báo stack s={n}
    Khai báo res = {n} để các giá trị
B2: Duyệt s.qsize()>0
    - Lấy u khỏi S
    - Phân tích u=a*b (a<=b)
        Sinh ra các v
        * Nếu v không thuộc res thì
            S.put(v)
            res.add(v)
B3: Lặp lại B2 tới khi S rỗng
B4: Xuất các phần tử res
'''

import queue
if __name__ == "__main__":
    n = int(input())
    S = queue.LifoQueue()
    S.put(n)
    res = {n}
    while S.qsize()>0:
        u = S.get()
        m = int(u**0.5)
        for a in range(1,m+1):
            if u%a == 0:
                b = (u//a)
                v = (a-1)*(b+1)
                if v not in res:
                    S.put(v)
                    res.add(v)
    print(*res)








