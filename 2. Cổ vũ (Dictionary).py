'''
- Đề bài:
Trong một cuộc thi tài có 2 đối thủ mặc đai xanh và đai đỏ thi đấu với nhau, để cổ vũ cho hai đối thủ thì các cổ động viên
đứng xếp thành một hàng dọc cổ vũ cho đối thủ nào thì tay cầm cờ mầu đai của đối thủ đó.Tichpx đi cổ vũ thi đấu thì gặp
một bạn cựu sinh viên ngày xưa học thuật toán do Tichpx dạy.
Tichpx đố bạn đó tìm một đoạn dài nhất liên tục các cổ động viên sao cho số cổ vũ cho đối thủ đai xanh bằng số cổ vũ cho đối thủ đai đỏ.
Bạn hãy giúp bạn cựu sinh viên đó nhé.
Bài toán đặt ra là nhập vào một xâu ký tự gồm những ký tự X biểu thị cho mầu Xanh và D biểu thị cho mầu Đỏ
chỉ ra độ dài đoạn dài nhất có số ký tự X bằng số ký tự D
- Input:
Một xâu có ít nhất một ký tự với độ dài không quá 10^6 gồm các ký tự 'X' hoặc 'D'
- Output:
Một số nguyên không âm là đoạn con liên tục dài nhất mà số ký tự X bằng số ký tự D

- Ví dụ:
Input:
XXDXDXX
Output:
4
*Giải thích : Đoạn dài nhất là XDXD hoặc DXDX cân bằng số ký tự D và X đều bằng 2
'''

'''
1. Ý tưởng thuật toán:
- Biến đếm t để theo dõi sự chênh lệch giữa số lượng 'X' và 'D'.
- Từ điển D để lưu trữ vị trí xuất hiện đầu tiên của mỗi giá trị cân bằng.
- Biến res để lưu trữ độ dài lớn nhất của đoạn cân bằng.
2. Các Bước Triển Khai:
B1: Khởi tạo biến t = 0, D = {0: 0} và res = 0.
B2: Duyệt qua từng ký tự của xâu a. 
    Tăng giảm t tùy thuộc vào ký tự là 'X' hay 'D' ('X' t tăng 1, 'D' t giảm 1).
B3: Nếu t chưa xuất hiện trong D, ghi nhận vị trí hiện tại của nó.
         => D[t] = i
    Nếu t đã xuất hiện, cập nhật res bằng độ dài lớn nhất của đoạn từ vị trí đó đến vị trí hiện tại. 
        => res = max(res, i - D[t])
B4: Cuối cùng, in ra giá trị của res.
'''

if __name__ == "__main__":
    s = input()
    t=0
    D = {0: 0}
    res = 0
    for i,x in enumerate(s,1):
        if x == 'X':
            t+=1
        else:
            t-=1
        if t not in D:
            D[t] = i
        else:
            res = max(res,i-D[t])
    print(res)

