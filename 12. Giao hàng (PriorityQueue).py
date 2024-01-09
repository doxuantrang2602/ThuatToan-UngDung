'''
- Đề bài:
Khi đại dịch Covid-19 tràn đến, cả nước áp dụng chính sách cách ly toàn xã hội, mọi người hạn chế ra ngoài.
Nhiều người nhận thấy đây là cơ hội kinh doanh tốt và nhanh chóng thành lập công ty vận chuyển hàng hóa giao tận nơi cho khách hàng.
Titi là một nhân viên giao hàng cho một công ty lớn, chính sách của công ty này là cứ giao hàng mà trước một thời hạn cho trước sẽ
được thưởng tùy theo món hàng mà nhân viên đó giao.
* Titi nhận được n món hàng cần giao, món hàng thứ i giao không trễ quá thời giao t[i] sẽ được thưởng tiền.
  Giả sử cứ một đơn vị thời gian thì Titi giao được một món hàng, bạn hãy giúp Titi xếp thứ tự giao hàng thế nào
  để được nhiều tiền thưởng nhất nhé
- Input:
+) Dòng đầu số nguyên dương n là số món hàng Titi phải giao (1<=n<=1000)
+) Tiếp theo n dòng mỗi dòng chứa hai giá trị là ti và vi nếu món hàng này Titi giao không trễ quá ti thì sẽ được thưởng vi
   trong đó 1<=ti,vi<=10^6
- Output:
=> Số tiền được thưởng cao nhất có thể nếu Titi chọn được cách giao hợp lý nhất.

- Ví dụ:
Input
6
3 5
3 7
1 3
2 4
2 2
4 1
Output:
17
* Giải thích:
Đề dễ giải thích ta cứ gọi đơn vị thời gian là giờ. Chúng ta có 6 món đồ chuyển cách chuyển như sau sẽ được 17 tiền:
- Giờ thứ nhất chuyển món thứ tư có thời hạn trong 2 giờ nhưng giao luôn giờ thứ nhất bạn được thưởng 4 tiền
- Giờ thứ hai và ba chuyển món thứ nhất và thứ hai có thời hạn trong 3 giờ bạn giao một món đúng giờ
  và một món sớm giờ tổng cộng 12 tiền thưởng
- Giờ thứ tư tất nhiên bạn giao món thứ sáu thời hạn trong 4 giờ và bạn vẫn kịp bỏ túi 1 tiền thưởng
'''

'''
1. Ý tưởng thuật toán 
- Thuật toán dựa trên việc sử dụng hàng đợi ưu tiên để lựa chọn món hàng có thưởng lớn nhất có thể giao 
  trong mỗi khoảng thời gian cho phép. 
- Mảng A được sử dụng để lưu trữ các giá trị thưởng (vi) của từng món hàng tại thời hạn (ti) tương ứng. 
- Bắt đầu từ thời hạn lớn nhất, thuật toán sẽ chọn món hàng có giá trị thưởng lớn nhất có thể giao tại mỗi khoảng thời gian.
2. Triển khai thuật toán
B1: Nhập n
B2: Khởi tạo mảng A lưu thời gian ti tương ứng vi 
    PQ>0
    M=0 để tìm max(ti)
    Hàng đợi ưu tiên PQ>0
    res=0 để lưu kết quả 
B3: Duyệt i từ 0->n-1
    Nhập ti,vi
    A[ti].add(vi)
    Tìm M = max(ti)
B4: Duyệt thời gian từ M về 1
    - Đưa các giá trị A[t] vào Q
    - Nếu Q khác rỗng thì res+=Q.get()
B5: In ra kết quả res
'''
import queue
if __name__ == "__main__":
    n = int(input())
    A = [[] for i in range(100005)]
    PQ = queue.PriorityQueue()
    M = 0
    res = 0
    for i in range(n):
        t,v = map(int,input().split())
        A[t].append(v)
        if M<t:
            M=t
    for i in range(M,0,-1):
        for x in A[i]:
            PQ.put(-x)
        if PQ.qsize()>0:
            res += -PQ.get()
    print(res)


