import os,sys
from os.path import expanduser

MAIN_DIR = expanduser("/etc/hosts")

def setup(repo):
	if repo == "/":
		os.system('./permissions.sh')

def add_new_website():
	target = open(MAIN_DIR,'a')
	web = raw_input("Enter the website you want to block: ")
	blank = "     "
	target.write('%s%s%s' % ("127.0.0.1",blank,web) )
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
	target.close

def remove_website():
	print "Here is the list of urls you have blocked Select the number of the particular url you want to unblock"
	show_list()
	number = raw_input("Enter the number of the url from the list shown above to unblock it")
	numb = int(number) - 1
	target = open(MAIN_DIR,'r+')
	content = target.readlines()
	count = len(content)
	list_site = []
	for i in range(count):
		numbering = i+1
		temp = content[i]
		url = temp.split(" ")[5]
		list_site.append(url)
	web_value = list_site[numb]
	list_site.remove(web_value)
	target.close
	target = open(MAIN_DIR,'w')
	for i in range(len(list_site)):
		web = list_site[i]
		blank = "     "
		target.write('%s%s%s' % ("127.0.0.1",blank,web) )
	target.close




def main():
	print "Welcome to firewall. Customize it your own way!! \n"
	option = raw_input("Select one of the following :- \n1) Want to add new website to block in on your system. \n2) Want to remove blocked website from your system. \n3) Want to see the block websites list.")
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
