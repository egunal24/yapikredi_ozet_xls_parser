from pandas import read_excel
import datetime

class ExcelProcessor:

    def __init__(self,filepath):
        self.df = read_excel(filepath)
        self.money_col = self.df["Unnamed: 6"][10:] #this reads the column with the money.
        self.sum = sum(self.money_col)

        self.l = []
        self.filtered_sum = 0
    
    def filter(self,scale):
        for money in self.money_col:
            if abs(money) <= scale: self.l.append(money)
        self.filtered_sum = sum(self.l)

    def calculate_days(self):
        date_col = self.df["Hesap Hareketleri"]
        end_date = datetime.datetime.strptime(date_col[10],"%d/%m/%Y")
        start_date = datetime.datetime.strptime(date_col[len(date_col)-1],"%d/%m/%Y")
        date_diff = end_date - start_date
        return date_diff.days

    def show(self):
        scale = float(input("Input a positive numerical value to filter transactions by:"))
        self.filter(scale)
        days = self.calculate_days()

        print("---------------------------------------------------------------------")
        print("------------------------TRANSACTIONAL HISTORY------------------------")
        print("---------------------------------------------------------------------")
        print(f"Total money delta in {days} days equals: {self.filtered_sum}")
        print(f"Average money delta per day equals: {self.filtered_sum/days}")
        print("---------------------------------------------------------------------")