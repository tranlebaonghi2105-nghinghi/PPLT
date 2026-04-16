#vòng lặp for và cập nhật trạng thái
n = int(input("Nhập n: "))

tong_chan = 0
tong_le = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        tong_chan += i
    else:
        tong_le += i

print("Tổng chẵn:", tong_chan)
print("Tổng lẻ:", tong_le)