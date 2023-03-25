import json
import os

# JSON dosyası yaratma
def create_json_file():
    data = {}
    with open("stok.json", "w") as f:
        json.dump(data, f)

# JSON dosyasından stokları okuma
def read_stocks():
    if os.path.exists("stok.json"):
        with open("stok.json", "r") as f:
            stocks = json.load(f)
    else:
        create_json_file()
        stocks = read_stocks()
    return stocks

# Stokları yazdırma
def print_stocks():
    stocks = read_stocks()
    for product, stock in stocks.items():
        print(f"{product}: {stock}")

# Yeni stok ekleme
def add_stock():
    stocks = read_stocks()
    product_name = input("Ürün adını giriniz: ")
    product_stock = input("Ürün stokunu giriniz: ")
    stocks[product_name] = int(product_stock)
    with open("stok.json", "w") as f:
        json.dump(stocks, f)
    print(f"{product_name} ürününe {product_stock} adet stok eklendi.")

# Stok silme
def remove_stock():
    with open("stok.json", "r+") as f:
        stocks = json.load(f)
        print("=== Stok Silme ===")
        print("1. Hepsini Sil")
        print("2. Belirli Bir Miktar Sil")
        choice = int(input("Seçim yapın (1 veya 2): "))
        if choice == 1:
            confirmation = input("Tüm stokları silmek istediğinizden emin misiniz? (E/H): ")
            if confirmation.upper() == "E":
                stocks.clear()
                f.seek(0)
                json.dump(stocks, f)
                f.truncate()
                print("Tüm stoklar silindi!")
        elif choice == 2:
            product = input("Silmek istediğiniz ürünü girin: ")
            if product in stocks:
                quantity = int(input("Silmek istediğiniz miktarı girin: "))
                if quantity > stocks[product]:
                    print(f"{product} stokta yeterli miktarda bulunmuyor.")
                elif quantity == stocks[product]:
                    del stocks[product]
                    f.seek(0)
                    json.dump(stocks, f)
                    f.truncate()
                    print(f"{product} stoktan silindi!")
                else:
                    stocks[product] -= quantity
                    f.seek(0)
                    json.dump(stocks, f)
                    f.truncate()
                    print(f"{product} stoktan {quantity} adet silindi.")
            else:
                print(f"{product} stokta bulunamadı.")
        else:
            print("Geçersiz seçim!")

# Kullanıcı girişi kontrolü
def admin_login():
    username = input("Kullanıcı adınızı giriniz: ")
    password = input("Şifrenizi giriniz: ")
    if username == "admin" and password == "12345":
        return True
    else:
        return False

# Ana menü
def main_menu():
    while True:
        print("\nLütfen yapmak istediğiniz işlemi seçiniz:")
        print("1- Stokları görüntüle")
        print("2- Yeni stok ekle")
        print("3- Stok sil")
        print("4- Çıkış yap")
        choice = input("Seçiminiz: ")
        if choice == "1":
            print_stocks()
        elif choice == "2":
            if admin_login():
                add_stock()
            else:
                print("Hatalı kullanıcı adı veya şifre!")
        elif choice == "3":
            if admin_login():
                remove_stock()
            else:
                print("Hatalı kullanıcı adı veya şifre!")
        elif choice == "4":
            break
        else:
            print("Geçersiz seçim!")

# Programın ana fonksiyonu
def main():
    main_menu()

# Programı çalıştırma
if __name__ == "__main__":
    main()
