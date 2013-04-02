#!/usr/bin/python
#gmail checker 
import mechanize
from BeautifulSoup import BeautifulSoup
import getpass
def main():
	Email='manimaran990@gmail.com'
	Passwd=getpass.getpass()
	br=mechanize.Browser()
	br.open('http://mail.google.com')
#print br.geturl()
	get_form=br.forms().next()
	get_form['Email']=Email
	get_form['Passwd']=Passwd
	resp2=br.open(get_form.click())
#print br.geturl()
#resp2=br.open(br.geturl())
	html=resp2.read()
	soup=BeautifulSoup(html)
	trs=soup.findAll('tr',{'bgcolor':'#ffffff'})
	for td in trs[:10]:
		print td.b.contents[0]+" : "+td.a.b.contents[0]

if __name__=='__main__':
	main()
