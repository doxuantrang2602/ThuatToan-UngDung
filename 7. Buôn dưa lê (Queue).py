'''
- Đề bài:
Đại dịch covid-19 ùa đến quá nhanh, làng Quẹo trồng rất nhiều dưa lê nhưng mọi người phải đi cách ly nên không có ai thu hoạch.
Tito quyết định dồn tiền mua hết dưa lê của cả cánh đồng Quẹo. . Cách đồng Quẹo có n thửa ruộng được đánh số từ 1 đến n,mỗi thửa ruộng
thứ i thì bắt đầu được thu hoạch từ ngày thứ thứ i nếu thu hoạch đúng trong vòng k ngày sẽ thu được sản lượng là a[i] nếu quá k ngày
thì dưa lê sẽ bị hỏng. Mà năng lực có hạn nên mỗi ngày Tito chỉ thu hoạch được tối đa m sản lượng.
Bạn hãy tính tổng sản lượng có thể lớn nhất mà TiTo thu hoạch trên cánh đồng này.
- Input:
+) Dòng đầu chứa n, k, m tương ứng là số thửa ruộng, số ngày tối đa mà dưa phải thu hoạch cho mỗi thửa và năng lực của Tito
   (1<= n,k,m <=10^5)
+) Dòng thứ 2 chứa n giá trị là sản lượng lần lượt dưa lê chín trong từng ngày từ 1 đến n các giá trị a[i]
   với (1<= a[i] <=10^9)
- Output:
=> Một số nguyên duy nhất là tổng tối đa sản lượng mà Tito có thể thu hoạch được

- Ví dụ:
Input
6 2 5
4 7 2 18 1 10
Output
33

* Giải thích :
Có 6 thửa ruộng, từ khi dưa lê bắt đầu chín thì chỉ được thu hoạch trong vòng 2 ngày và năng lực thu hoạch
mỗi ngày chỉ là 5 đơn vị sản lượng
- Ngày 1 dưa lê chín 4 mà năng lực 5 nên Tito sẽ thu được 4
- Ngày 2 dưa lê chín 7 mà năng lực 5 nên Tito sẽ thu được 5 còn lại 2 để sang ngày 3
- Ngày 3 dưa lê chín 2 cộng thêm 2 của ngày trước (chưa hỏng) mà năng lực 5 nên Tito sẽ thu được 4
- Ngày 4 dưa lê chín 18 mà năng lực 5 nên chỉ thu được 5 còn thừa 13 để sang ngày 5
- Ngày 5 Tito tập trung thu hoạch 5 của ngày 4 vì để quá 2 ngày sẽ hỏng nên 13 này chỉ thu được 5 còn lại phải bỏ đi,
  như vậy chỉ có 1 sản lượng chín vào ngày này đành để lại sang ngày 6 thu hoạch
- Ngày 6 Tito thu hoạch 1 sản lượng chín từ ngày 5 và 4 sản lượng chín từ ngày 6 nên sẽ được 5 sản lượng do đó còn 6 sản lượng để sang ngày 7
- Ngày 7 Tito sẽ thu hoạch 5 sản lượng chín từ ngày 6 tất nhiên 1 sản lượng còn lại sẽ bị hỏng
=> Như vậy tổng số sản lượng Tito thu được là 4+5+4+5+5+5+5 = 33
'''

'''
1. Ý tưởng thuật toán
- Sử dụng cấu trúc dữ liệu hàng đợi để lưu trữ sản lượng dưa lê từng ngày và thực hiện quá trình thu hoạch.
- Duyệt qua từng thửa ruộng, thêm sản lượng của thửa ruộng đó vào hàng đợi.
- Trong khi hàng đợi có quá nhiều phần tử (lớn hơn k), loại bỏ phần tử đầu tiên để giữ cho hàng đợi có k phần tử.
- Tính tổng sản lượng thu hoạch có thể lớn nhất theo yêu cầu của đề bài.
2. Triển khai thuật toán
B1: Nhập n, k, m
B2: Khai báo mảng list a, Queue Q, res = 0
B2: Duyệt dãy a:
    - Thêm sản lượng ngày hiện tại vào hàng đợi Q: Q.put(x)
    - Bỏ hết những thửa có quả hỏng (bị quá hạn):
        while Q.qsize()>k:
            Q.get()
    - Khởi tạo t=0 tương ứng lượng thu hoạch được trong ngày 
    - Chừng nào còn đủ năng lực m thì lấy hết quả của các thửa
    - Không thì lấy đủ năng lực, còn thừa thì để lại sang hôm sau
B3: In ra res
'''

import queue
if __name__ == "__main__":
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    Q = queue.Queue()
    a = a+[0]*(k-1)
    res = 0
    for x in a:
        Q.put(x)
        while Q.qsize()>k:
            Q.get()
        t = 0
        while Q.qsize()>0 and Q.queue[0]+t <=m:
            t += Q.get()
        if Q.qsize()>0:
            Q.queue[0] -= (m - t)
            t = m
        res+=t
    print(res)
