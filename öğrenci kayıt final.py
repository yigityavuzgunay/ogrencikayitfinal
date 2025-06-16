
import mysql.connector


class Ogrenci:
    def __init__(self, ad, soyad, numara, bolum):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.bolum = bolum


class Veritabani:
    def __init__(self):
        self.baglanti = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="",  
            database="ogrenci_sistemi",
            charset='utf8'
        )
        self.cursor = self.baglanti.cursor()

    def ogrenci_ekle(self, ogrenci):
        sql = "INSERT INTO ogrenciler (ad, soyad, numara, bolum) VALUES (%s, %s, %s, %s)"
        veri = (ogrenci.ad, ogrenci.soyad, ogrenci.numara, ogrenci.bolum)
        self.cursor.execute(sql, veri)
        self.baglanti.commit()
        print(" ogrenci eklendi.")

    def ogrencileri_listele(self):
        self.cursor.execute("SELECT * FROM ogrenciler")
        sonuc = self.cursor.fetchall()
        if not sonuc:
            print("Kayitli ogrenci bulunamadi.")
        for s in sonuc:
            print(f"ID:{s[0]} | {s[1]} {s[2]} | No: {s[3]} | Bölüm: {s[4]}")

    def ogrenci_guncelle(self, id, yeni):
        sql = "UPDATE ogrenciler SET ad=%s, soyad=%s, numara=%s, bolum=%s WHERE id=%s"
        veri = (yeni.ad, yeni.soyad, yeni.numara, yeni.bolum, id)
        self.cursor.execute(sql, veri)
        self.baglanti.commit()
        print("Öğrenci güncellendi.")

    def ogrenci_sil(self, id):
        sql = "DELETE FROM ogrenciler WHERE id=%s"
        self.cursor.execute(sql, (id,))
        self.baglanti.commit()
        print(" Öğrenci silindi.")

def menu():
    print("""
 ÖĞRENCİ KAYIT SİSTEMİ 
1 - Öğrenci Ekle
2 - Öğrencileri Listele
3 - Öğrenci Güncelle
4 - Öğrenci Sil
5 - Çikiş
""")


def main():
    vt = Veritabani()

    while True:
        menu()
        secim = input("Seçiminiz: ")

        if secim == "1":
            ad = input("Ad: ")
            soyad = input("Soyad: ")
            numara = input("Numara: ")
            bolum = input("Bölüm: ")
            ogr = Ogrenci(ad, soyad, numara, bolum)
            vt.ogrenci_ekle(ogr)

        elif secim == "2":
            vt.ogrencileri_listele()

        elif secim == "3":
            id = input("Güncellenecek öğrencinin ID'si: ")
            ad = input("Yeni Ad: ")
            soyad = input("Yeni Soyad: ")
            numara = input("Yeni Numara: ")
            bolum = input("Yeni Bölüm: ")
            yeni = Ogrenci(ad, soyad, numara, bolum)
            vt.ogrenci_guncelle(id, yeni)

        elif secim == "4":
            id = input("Silinecek öğrencinin ID'si: ")
            vt.ogrenci_sil(id)

        elif secim == "5":
            print("Programdan cikiliyor...")
            break

        else:
            print("Geçersiz seçim. Tekrar dene.")

if __name__ == "__main__":
    main()