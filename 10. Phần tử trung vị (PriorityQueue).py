'''
- Đề bài:
Tichpx dạy môn xử lý ảnh có thuật toán lọc trung vị, đây là một thuật toán cần phải tìm trung vị của histogram.
Trung vị của một dãy n phần tử a1,a2,...,an là phần tử mà khi sắp xếp dãy tăng dần thì nó ở giữa dãy đó là a[(n+1)/2].
Chẳng hạn trung vị của dãy {1,3,4,5} có 4 phần tử trung vị là a[(4+1)/2]=a[2]= 3 còn trung vị của dãy {1,3,4,5,5}
thì trung vị là a[(5+1)/2]=a[3]=4;
Bài toán đặt ra là bạn lần lượt bổ sung n phần tử vào dãy với mỗi phần tử thứ i bổ sung vào thì xuất ra trung vị của dãy con a1,a2,...,ai
- Input:
Dòng đầu là số nguyên dương n (1<=n<=10^6)
Dòng tiếp theo chứa n phần tử có giá trị tuyệt đối không vượt quá 32767.
- Output:
Xuất ra n giá trị trung vị của các dãy con tiếp đầu của dãy đã cho

- Ví dụ:
Input:
9
7 4 2 1 6 8 5 8 7
Output:
7 4 4 2 4 4 5 5 6
* Giải thích : Ban đầu dãy rỗng ta bổ sung lần lượt
- Bổ sung 7 nên dãy con sau khi săp {7} -> trung vị 7
- Bổ sung 4 nên dãy con sau khi săp {4, 7} -> trung vị 4
- Bổ sung 2 nên dãy con sau khi sắp {2, 4, 7} -> trung vị 4
- Bổ sung 1 nên dãy con sau khi sắp {1, 2, 4, 7} -> trung vị 2
- Bổ sung 6 nên dãy con sau khi sắp {1, 2, 4, 6, 7} -> trung vị 4
- Bổ sung 8 nên dãy con sau khi sắp {1, 2, 4, 6, 7, 8} -> trung vị 4
- Bổ sung 5 nên dãy con sau khi sắp {1, 2, 4, 5, 6, 7, 8} -> trung vị 5
- Bổ sung 8 nên dãy con sau khi sắp {1, 2, 4, 5, 6, 7, 8, 8} -> trung vị 5
- Bổ sung 7 nên dãy con sau khi sắp {1, 2, 4, 5, 6, 7, 7, 8, 8} -> trung vị 6
'''

'''
1. Ý tưởng thuật toán
- Cấu trúc để lưu input:
 => Sử dụng PriorityQueue để lưu 2 hàng đợi ưu tiên L và R. 
 Trong đó L để lưu các phần tử ở vị trí lẻ (đánh số từ 1,...)
          R để lưu các phần tử ở ví trí chẵn
2. Triển khai thuật toán
B1: Nhập n, a1,a2,...,an 
B2: Khởi tạo 2 PriorityQueue L và R rỗng
B3: Duyệt phần tử x theo chỉ số i từ 1
    - Nếu phần tử ở vị trí lẻ => L.put(-x)
    - Ngược lại, nếu phần tử ở vị trí chẵn => R.put(x)
    - Nếu chỉ số > 1 và Max của L (-L.queue[0]) lớn hơn Min của R (R.queue[0])
      => Tráo đổi vị trí cho nhau
    - In ra kết quả: Max của L (-L.queue[0])
'''
import queue
if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    L = queue.PriorityQueue()
    R = queue.PriorityQueue()
    for i,x in enumerate(a,1):
        if i%2 == 1:
            L.put(-x)
        else:
            R.put(x)
        if i>1 and -L.queue[0]>R.queue[0]:
            u,v = -L.get(), R.get()
            L.put(-v)
            R.put(u)
        print(-L.queue[0], end = " ")


