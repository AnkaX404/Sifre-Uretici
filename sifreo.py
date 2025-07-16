import string
import random
import colorama
from colorama import Fore, Style, init
init(autoreset=True)
import os

## Şifreleri İncele ##
def sifreleri_incele():
	os.system('clear')
	with open("sifreler.txt", "r", encoding="utf-8") as dosya:
		oku = dosya.read()
		print(Fore.LIGHTGREEN_EX + oku)
######################

## Şifre Kaydetme Fonksiyonu ##
def sifre_olustur():
	isim = input("Şifrenin Hangi Uygulamaya veya Siteye Ait Olacak: ")
	rast_karakter = string.ascii_letters + string.digits + string.punctuation
	sifre = ""
	i = 0
	while i < 18:
		sifre += random.choice(rast_karakter)
		i += 1
	with open("sifreler.txt", "a", encoding="utf-8") as dosya2:
		dosya2.write(f"\n{isim}: {sifre}\n")
	print(Fore.LIGHTGREEN_EX + "\nŞifre Dosyaya Yazıldı ✅")
#########################

## Giriş Menüsü ##
def ana_menu():
	while True:
		os.system('clear')
		print(Fore.LIGHTGREEN_EX + "Kayıtlı Şifreleri Görmek İçin: [1]")
		print(Fore.LIGHTGREEN_EX + "Yeni Bir Güçlü Şifre Oluşturmak İçin: [2]")
	
		secim = input("\nYapmak İstediğin İşlemi Seç: ")

		if secim == "1":
			os.system('clear')
			sifreleri_incele()
	
		elif secim == "2":
			os.system('clear')
			sifre_olustur()
		input("\nGeri Dönmek İçin Enter'a Bas.")
#########################

ana_menu()