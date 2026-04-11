from pandas import read_excel
import datetime

class ExcelProcessor:

    def __init__(self):
        print("---------------------------------------------------------------------")
        print("---------------------------THE GRAND PARSER--------------------------")
        print("---------------------------------------------------------------------")

        filepath = input("Please enter a valid filename to the .xls file to read:")
        self.flag = False
        try:
            self.df = read_excel(filepath)

            self.money_col = self.df["Unnamed: 6"].iloc[10:]
            self.l = []
            self.filtered_sum = 0
        except:
            print("Invalid input, file may not exist. Please restart program with a proper filepath.")
            self.flag = True

    def filter(self,scale):
        self.l = []
        self.filtered_sum = 0
        for money in self.money_col:
            if abs(float(money)) <= scale: self.l.append(float(money))
        for elem in self.l:
            self.filtered_sum += float(elem)

    def calculate_days(self):
        date_col = self.df["Hesap Hareketleri"]
        end_date = datetime.datetime.strptime(date_col[10],"%d/%m/%Y")
        start_date = datetime.datetime.strptime(date_col[len(date_col)-1],"%d/%m/%Y")
        date_diff = end_date - start_date
        return date_diff.days

    def show(self):
        if self.flag:
            return
        scale = float(input("Input a positive numerical value to filter transactions by:"))
        self.filter(scale)
        days = self.calculate_days()

        print("---------------------------------------------------------------------")
        print("------------------------TRANSACTIONAL HISTORY------------------------")
        print("---------------------------------------------------------------------")
        print(f"Total money delta in {days} days equals: {self.filtered_sum}")
        print(f"Average money delta per day equals: {self.filtered_sum/days}")
        print("---------------------------------------------------------------------")
        print("---------------------------------------------------------------------")
        print("---------------------------------------------------------------------")
