from res import ExcelProcessor

def main():
    e = ExcelProcessor("Hesap_Hareketleri.xls")
    e.filter(1000)
    e.show()

if __name__ == "__main__":
    main()