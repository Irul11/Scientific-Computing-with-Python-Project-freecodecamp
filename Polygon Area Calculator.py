class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.swidth = 0
        self.sheight = 0
        self.shape = 0

    def set_width(self, swidth):
        self.swidth = swidth
        self.width = swidth
        return swidth

    def set_height(self, sheight):
        self.sheight = sheight
        self.height = sheight
        return sheight

    def get_area(self):
        area = self.width*self.height
        return area

    def get_perimeter(self):
        perim = (self.width * 2) + (self.height * 2)
        return perim

    def get_diagonal(self):
        diag = (self.width ** 2 + self.height ** 2) ** .5
        return diag

    def get_picture(self):
        pict = ""
        lebar = self.width
        panjang = self.height
        if lebar <= 50 and panjang <= 50:
            for i in range(panjang):
                pict += "*" * lebar
                pict += "\n"
        else:
            pict += "Too big for picture."
        return pict

    def get_amount_inside(self, shape):
        self.shape = shape
        lebar_luar = self.width
        lebar_dalam = shape.width
        panjang_luar = self.height
        panjang_dalam = shape.height
        amount = (lebar_luar//lebar_dalam)*(panjang_luar//panjang_dalam)
        return amount

    def __repr__(self):
        x = "Rectangle(width={}, height={})".format(self.width, self.height)
        return x


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.sisi = 0

    def set_side(self, sisi):
        self.sisi = sisi
        self.width = sisi
        self.height = sisi
        return sisi

    def __repr__(self):
        x = "Square(side={})".format(self.width)
        return x


# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())
#
# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())
#
# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))
