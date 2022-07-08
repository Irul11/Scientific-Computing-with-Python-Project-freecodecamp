class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.spent = 0
        self.desc = ''
        self.destination = ''
        self.amount = 0.

    def deposit(self, amount, desc=''):
        self.desc = desc
        self.amount = amount
        depos = {'amount': amount, 'description': desc}
        self.ledger.append(depos)
        return depos

    def withdraw(self, amount=0., desc=''):
        self.desc = desc
        self.amount = amount
        if not self.check_funds(amount):
            return
        self.spent += amount
        wdraw = {'amount': amount * (-1), 'description': desc}
        self.ledger.append(wdraw)
        return wdraw

    def transfer(self, amount, destination):
        self.amount = amount
        self.destination = destination
        y = 'Transfer to {}'.format(destination.name)
        self.withdraw(amount, y)
        # trnsfr = {'amount': amount*(-1), 'description' : y}
        # self.ledger.append(z) nggk perlu lagi, soalnya udah otomatis pake fungsi withdraw
        return destination.deposit(amount, 'Transfer from ' + self.name)

    def check_funds(self, amount):
        fund = 0
        for i in self.ledger:
            fund += i['amount']
            if fund < amount:
                return False
            else:
                return True

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        # for i in ledger:
        return balance

    def __repr__(self):
        # z = ""
        x = "{:*^30}\n".format(self.name)
        for i in self.ledger:
            x += "{:<23.23}{:7.2f}\n".format(i['description'], i['amount'])
        x += "Total: {:.2f}".format(self.get_balance())
        return x


# fungsi vertikal
def vertical(s):
    maks = 0
    for h in s:
        if len(h) > maks:
            maks = len(h)
    for o in range(len(s)):
        s[o] += " " * (maks - len(s[o]))
    row = [""] * maks

    # Buat matriks baru buat tranpose matriks
    sell = []
    for ab in range(maks + 3):
        sell += [[]]
        sell[ab] += row
    # Buat list matriks buat ditranspose
    g = [["100", ' 90', ' 80', ' 70', ' 60', ' 50', ' 40', ' 30', ' 20', ' 10', '  0'], ["|"] * 11]
    g[0] += ["  "] * (maks - 11)
    g[1] += ["  "] * (maks - 11)
    for i in range(len(s)):
        g += [[]]
        for j in range(len(s[i])):
            g[i + 2].append(s[i][j])
    teks = ""
    # Buat jadi vertikal
    for k in range(len(g)):
        for l in range(len(g[k])):
            sell[l][k] += g[k][l]

    for final in range(len(sell)):
        for fin in sell[final]:
            teks += fin
        teks += "\n"
    return teks


def create_spend_chart(categ):
    ss = []
    nam = []
    for j in categ:
        ss.append(j.spent)
        nam.append(j.name)
    total = sum(ss)
    list_per = []
    for i in ss:
        h = int((i * 100 / total) // 10)
        list_per.append(h)
    teks = []

    for i in range(len(ss)):
        teks += []
        teks = teks + [" " * 12 + "-"]
        kosong = " " * (10 - list_per[i])
        bulat = "o" * (list_per[i] + 1)
        teks += ['{}{}{}{}'.format(kosong, bulat, " -", nam[i])]
        teks = teks + [" " * 12 + "-"]
    teks = teks + [" " * 12 + "-"]
    akhir = "Percentage spent by category\n" + vertical(teks)
    return akhir


# For testing
# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# # print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print(create_spend_chart([food, clothing, auto]))
