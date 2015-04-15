import os,sys
from os.path import expanduser

MAIN_DIR = expanduser("/etc/hosts")

def add_new_website():
	target = open(MAIN_DIR,'a')
	web = raw_input("Enter the website you want to block: ")
	blank = "     "
	target.write('%s%s%s\n' % ("127.0.0.1",blank,web) )
	target.close

def show_list():
	target = open(MAIN_DIR,'r')
	content = target.readlines()
	count = len(content)
	for i in range(count):
		numbering = i+1
		temp = content[i]
		url = temp.split(" ")[5]
		print  "(", numbering, ") ",url 

def remove_website():
	target = open(MAIN_DIR,'a')

def main():
	print "Welcome to firewall. Customize it your own way!!"
	option = raw_input("Select one of the following :- 1) Want to add new website to block in on your system. 2) Want to remove blocked website from your system. 3) Want to see the block websites list.")
	if (option == '1'):
		add_new_website()
	elif (option == '2'):
		remove_website()
	elif (option == '3'):
		show_list()
	else:
		print "Selection only from the options provided"

if __name__ == '__main__':
    main()




