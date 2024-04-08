from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    def generateID(self):
        maxId = 1
        if self.soLuongSinhVien() > 0:
            maxId = self.listSinhVien[0].id
            for sv in self.listSinhVien:
                if maxId < sv.id:
                    maxId = sv.id
            maxId += 1
        return maxId
    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành của sinh viên: ")
        diemTB = float(input("Nhập điểm của sinh viên: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = input("Nhập chuyên ngành của sinh viên: ")
            diemTB = float(input("Nhập điểm của sinh viên: "))
            sv.name = name
            sv.sex = sex
            sv.major = major
            sv.diemTB = diemTB
            self.xepLoaiHocLuc(sv)
            print("Thông tin sinh viên đã được cập nhật.")
        else:
            print(f"Không tìm thấy sinh viên có ID {ID}.")
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x.id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x.name, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x.diemTB, reverse=False)

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def findByID(self, ID):
        searchResult = None
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if sv.id == ID:
                    searchResult = sv
                    break
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if keyword.upper() in sv.name.upper():
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    def xepLoaiHocLuc (self, sv: SinhVien): 
        if (sv. diemTB >= 8):
            sv._hocLuc= "Gioi"
        elif sv._diemTB >= 6.5:
            sv.hocLuc = "Kha"
        elif sv.diemTB >= 5:
            sv.hocLuc = "Trung bình"
        else:
            sv.hocLuc = "Yeu"
def showSinhVien(self, listSV):
    print("{:<8} {:<18} {:<8} {:<8} {:<8}"
          .format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
    if len(listSV) > 0:
        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<8} {:<8}"
                  .format(sv._id, sv._name, sv.sex, sv._major, sv._diemTB, sv.hocLuc))
        print("\n")

def getListSinhVien(self):
    return self.listSinhVien
