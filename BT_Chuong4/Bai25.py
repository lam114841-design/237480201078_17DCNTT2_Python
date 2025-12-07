def sap_xep_so_chan_0_le(L):
    """
    Hàm sắp xếp list L theo quy tắc:
    - số chẵn ở đầu
    - số 0 ở giữa
    - số lẻ ở cuối
    :param L:
    :return:
    """
    chan = [x for x in L if x != 0 and x % 2 == 0]
    khong = [x for x in L if x == 0]
    le = [x for x in L if x % 2 != 0]

    return chan + khong + le

#chạy
L = list(map(int, input("nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
ket_qua = sap_xep_so_chan_0_le(L)
print("List sau khi sắp xếp: ",ket_qua)