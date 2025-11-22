# student.py

class SinhVien:
    def __init__(self, ma, ten, tuoi, lop):
        self.ma = ma
        self.ten = ten
        self.tuoi = tuoi
        self.lop = lop

    def __str__(self):
        return f"{self.ma} - {self.ten} - {self.tuoi} tuổi - Lớp {self.lop}"
