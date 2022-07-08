import random
import copy


class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []

    def draw(self, draw):
        for key, value in self.kwargs.items():
            self.contents += [key]*value
        taken = []
        if draw > len(self.contents):
            taken = self.contents
        else:
            acak = random.sample(self.contents, draw)
            taken += acak
        return taken

    def __repr__(self):
        for key, value in self.kwargs.items():
            self.contents += [key]*value
        return str(self.contents)


# buat fungsi untuk menghitung apakah jumlah yg diharapkan sama dengan fakta
# s: dict dari yg diharapkan sedangkan sa: dict hasil random
def hitung(s, sa):
    amount = 0
    if (s.keys()) <= sa.keys():
        s_list = []
        sa_list = []
        for i in s.keys():
            s_list += [s[i]]
            sa_list += [sa[i]]
        if s_list <= sa_list:
            amount += 1
        else:
            amount += 0
    else:
        amount += 0
    return amount


# Buat fungsi lain untuk membuat list dikelompokkan sesuai warna
def kelompok(array):
    x = {}
    for i in array:
        if str(i) in x.keys():
            x[str(i)] += 1
        else:
            x[str(i)] = 1
    return x


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Buat list hasil random
    tes = []
    # f = hat.draw(num_balls_drawn)  # draw bola
    # print("hasil", f)
    # print(hat.draw(num_balls_drawn))
    for i in range(num_experiments):
        # Duplikat class Hat
        copied = copy.copy(hat)
        tes += [[]]
        tes[i] += copied.draw(num_balls_drawn)     # Memasukkan hasil random ke dalam list dengan indeks berbeda

    # Buat variabel yang mewakili jumlah probabilitas sukses
    amount = 0

    for i in tes:
        hasil_bola = kelompok(i)
        amount += hitung(expected_balls, hasil_bola)

    prob = amount/num_experiments
    return prob


# tt = Hat(red=1, blue=5)
# xx = Hat(red=3, blue=2)
# print(tt)
# print(xx)
