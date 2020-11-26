from urllib.request import urlopen

from bs4 import BeautifulSoup

import ssl

import re

html = []

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#beautiful soup parsing
url = input ('Enter the URL here: ')
location = int(input("Please enter the location (integer only) here: "))-1
Rep = int(input ("Please enter repetition # (integer only) here: "))
Rep_og = Rep

#to repeat the program
while Rep > 0:
    #url handle
    webhandle1 = urlopen(url, context=ctx).read()
    #beautiful soup parsing
    processedweb = BeautifulSoup(webhandle1, "html.parser")
    #finding tag "a"
    tags = processedweb('a')

    for tag in tags:
        tag = re.findall('http.+html', str(tag))
#making a list of the urls in the webpage to allow locating the correct one
        html.append(tag)

    #QUALITY INSURANCE
    print ("Rep#: ", Rep_og-Rep+1, html[location])

    #TRYING TO MAKE THE RESULT FEASIBLE TO BE FED INTO THE URL FIELD.......
    html_location = str(html(location))
    html_2_url = str(html_location)
    html_2_url= html_2_url.strip('[]')



#to feed the result back to input, track the progress, and reset the list
    url = html_2_url.encode()
    Rep = Rep - 1
    html = []
    print (tag)


#ERROR MESSAGE AS FOLLOWS
#Enter the URL here: http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Please enter the location (integer only) here: 3
#Please enter repetition # (integer only) here: 3
#Rep#:  1 ['http://py4e-data.dr-chuck.net/known_by_Montgomery.html']
#Traceback (most recent call last):
 # File "C:\Users\Zhidong Wang\Documents\python\crawler_mark2.py", line 34, in <module>
#    html_location = str(html(location))
#TypeError: 'list' object is not callable


#FOR some reason the data in the html list looks like this when printed: ['http://py4e-data.dr-chuck.net/known_by_Kieron.html'], ['http://py4e-data.dr-chuck.net/known_by_Filip.html'], ['http://py4e-data.dr-chuck.net/known_by_Dorothy.html'], ['http://py4e-data.dr-chuck.net/known_by_Kallan.html'], ['http://py4e-data.dr-chuck.net/known_by_Mena.html'], ['http://py4e-data.dr-chuck.net/known_by_Abbie.html'], ['http://py4e-data.dr-chuck.net/known_by_Amyleigh.html'], ['http://py4e-data.dr-chuck.net/known_by_Annalise.html'], ['http://py4e-data.dr-chuck.net/known_by_Carrich.html']
#I have no idea why there are brackets around each item......
