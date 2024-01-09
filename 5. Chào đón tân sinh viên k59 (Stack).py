'''
- Đề bài:
Nhân dịp chào đón các tân sinh viên K59 Đại học Giao thông vận tải, Nhà trường tổ chức các trò chơi trí tuệ cho các tân sinh viên
có một tinh thần thật thoải mái trước khi bước vào năm học. Trò chơi thú vị này có luật chơi như sau:
Có tất cả n sinh viên tham dự, xếp thành một hàng và mỗi bạn được đánh số từ 0 đến n - 1. Sau khi chỉ định bất kỳ bạn nào,
bạn đó sẽ phải chỉ ra chỉ số của bạn đứng gần mình nhất mà có chiều cao cao hơn mình, Nếu có nhiều chỉ số cùng thỏa mãn thì lấy
chỉ số bé hơn, nếu không có ai cao hơn thì chỉ số đó sẽ là -1.
Để trò chơi diễn ra thuận lợi và công bằng, Thầy TichPX giao cho đội tuyển Olympic tin học UTC viết một chương trình nhập vào
một dãy số nguyên a cho biết chiều cao của sinh viên ở từng chỉ số, và in ra dãy số nguyên khác thể hiện chỉ số cần tìm ở mỗi
vị trí trong dãy ban đầu.
Ví dụ: a = [1, 4, 2, 1, 7, 6] thì output sẽ là: b = [1, 4, 1, 2, -1, 4]
Với a[0] = 1 thì người cao hơn gần nhất là a[1] = 4 tại chỉ số là 1.
Với a[1] = 4 thì tương ứng chiều cao gần nhất là a[4] = 7 có chỉ số là 4.
Với a[2] = 2 thì người cao hơn gần nhất là a[1] = 4 tại chỉ số là 1.
Với a[3] = 1 thì người cao hơn gần nhất là a[2] = 2 tại chỉ số là 2.
Với a[4] = 7 thì không có ai cao hơn nên chỉ số là -1.
Với a[5] = 6 thì người cao hơn gần nhất là a[4] = 7 có chỉ số là 4.
- Input:
+) Dòng đầu tiên là n thể hiên số sinh viên (1<=n<=4*10^4)
+) Dòng thứ 2 bao gồm n số nguyên thể hiện chiều cao của n sinh viên. số thứ i thể hiên chiều cao của sinh viên thứ i
   (0<=i<n)
- Output:
=> Dòng duy nhất in ra n số nguyên. Số thứ i tương ứng là chỉ số của sinh viên gần nhất cao hơn sinh viên thứ i trong dãy đã cho.
- Ví dụ:
Input:
6
1 4 2 1 7 6
Output:
1 4 1 2 -1 4
'''

'''
1. Ý tưởng thuật toán
- Sử dụng cấu trúc dữ liệu Stack để tìm ra chỉ số của sinh viên gần nhất và cao hơn.
- Đặt hai Stack L và R để lưu thông tin về chỉ số và chiều cao của sinh viên bên trái và bên phải của sinh viên đang xét.
- Duyệt qua từng sinh viên từ trái sang phải để xác định chỉ số của sinh viên gần nhất và cao hơn bên trái.
- Duyệt qua từng sinh viên từ phải sang trái để xác định chỉ số của sinh viên gần nhất và cao hơn bên phải.
2. Triển khai thuật toán
B1: Nhập số lượng sinh viên n và danh sách chiều cao a của các sinh viên.
B2: Khởi tạo 2 hàng đợi LifoQueue QL và QR
    Khởi tạo 2 mảng rỗng L và R
    Khởi tạo mảng ans để lưu kết quả 
B3: Duyệt từ trái sang phải, sử dụng QL để xác định chỉ số của sinh viên cao hơn và gần nhất ở bên trái. 
    => Lưu kết quả vào danh sách L.
B4: Duyệt từ phải sang trái, sử dụng QR để xác định chỉ số của sinh viên cao hơn và gần nhất ở bên phải. 
    => Lưu kết quả vào danh sách R (đảo ngược danh sách sau khi duyệt).
B5: Duyệt qua từng sinh viên, 
    - So sánh chỉ số từ L và R để tìm chỉ số thấp nhất thỏa mãn. 
    - Lưu kết quả vào danh sách ans.
B6: In ra danh sách ans là output cuối cùng.
'''
import queue
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    QL = queue.LifoQueue()
    QR = queue.LifoQueue()
    L = []
    R = []
    ans = []
    QL.put([2e9, -1])
    for i in range(n):
        while QL.queue[-1][0] <= a[i]:
            QL.get()
        L.append(QL.queue[-1][1])
        QL.put([a[i], i])
    QR.put([2e9, -1])
    for i in range(n - 1, -1, -1):
        while QR.queue[-1][0] <= a[i]:
            QR.get()
        R.append(QR.queue[-1][1])
        QR.put([a[i], i])
    R.reverse()
    for i in range(n):
        if L[i] == -1 and R[i] == -1:
            ans.append(-1)
        elif L[i] == -1:
            ans.append(R[i])
        elif R[i] == -1:
            ans.append(L[i])
        else:
            if i - L[i] > R[i] - i:
                ans.append(R[i])
            else:
                ans.append(L[i])
    print(*ans)


