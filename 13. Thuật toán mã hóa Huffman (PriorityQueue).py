'''
- Đề bài:
Thuật toán mã hóa và nén dữ liệu Huffman là thuật toán mã hóa dữ liệu dựa trên mã tiền tố mã hóa không mất
thông tin văn bản rất hiệu quả
Bài toán hôm nay đặt ra là cho một xâu đầu vào chỉ gồm những chữ hoa tiếng Anh, bạn hãy cho biết sau khi
mã hóa Huffman thì tổng số bit là bao nhiêu
- Input:
Một xâu có độ dài không quá 10^5 ký tự hoa tiếng Anh
- Output:
Một số nguyên dương là tổng số bit sau khi mã hóa Huffman xâu ký tự đầu vào

- Ví dụ:
Input
GIAOTHONGVANTAI
Output
44
'''
import collections
import queue

'''
1. Ý tưởng thuật toán
- Sử dụng hàng đợi ưu tiên (PriorityQueue) để xây dựng cây Huffman.
- Đếm tần suất xuất hiện của mỗi ký tự trong xâu đầu vào.
- Tạo các node lá tương ứng với các ký tự và đưa vào hàng đợi ưu tiên.
- Xây dựng cây Huffman bằng cách kết hợp các node lá có tần suất thấp nhất.
- Tính tổng số bit sau khi mã hóa bằng cách cộng tần suất của mỗi ký tự với 
  sau mã hóa
2. Triển khai các bước
B1: Nhập xâu kí tự s 
    Khởi tạo F đếm tần xuất mỗi kí tự trong xâu đầu vào: F = Counter(s)
    Khởi tạo PQ
    res=0 để lưu kết quả tổng số bit
B2: Duyệt values f của F
    - Thêm tần suất các phần tử vào hàng đợi: PQ.put(f)
B3: Duyệt PQ.qsize()>1
    - Lấy ra tổng 2 tần suất nhỏ nhất: x=PQ.get() + PQ.get()
    - Cập nhật res+=x
    - PQ.put(x)
B4: In ra kết quả res
'''

import queue
import collections
if __name__ == "__main__":
    s = input()
    F = collections.Counter(s)
    PQ = queue.PriorityQueue()
    res = 0
    for f in F.values():
        PQ.put(f)
    while PQ.qsize()>1:
        x = PQ.get() + PQ.get()
        res += x
        PQ.put(x)
    print(res)



