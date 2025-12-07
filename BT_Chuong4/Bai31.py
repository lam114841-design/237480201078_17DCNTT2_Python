def key_max_value(d):
    """
    Hàm tìm và trả về key có giá trị lớn nhất trong dictionary d.
    """
    return max(d, key=d.get)


# --- Chạy thử ---
data = {"a": 10, "b": 25, "c": 7, "d": 30}
print("Key có giá trị lớn nhất là:", key_max_value(data))
