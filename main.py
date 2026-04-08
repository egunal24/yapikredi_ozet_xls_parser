from res import ExcelProcessor

def main():
    e = ExcelProcessor("Hesap_Hareketleri.xls")
    e.filter(1000)
    print(e.filtered_sum)

if __name__ == "__main__":
    main()

