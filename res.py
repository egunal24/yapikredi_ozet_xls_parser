from pandas import read_excel

class ExcelProcessor:

    def __init__(self,filepath):
        self.df = read_excel(filepath)
        self.money_col = self.df["Unnamed: 6"][10:] #this reads the column with the money.
        self.sum = sum(self.money_col)

        self.l = []
        self.filtered_sum = 0
        print(self.money_col)
    
    def filter(self,scale):
        for money in self.money_col:
            if abs(money) <= scale: self.l.append(money)
        self.filtered_sum = sum(self.l)