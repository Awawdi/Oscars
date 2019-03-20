#So I wanted to check what is the most common word in Oscars 2019 ceremony speeches.

#Transcripts of all Academy Awards winners' onstage speeches can be found here:
#https://lnkd.in/dEPuGSz

#Small Python program needed to extract all the links from the website, using #BeautifulSoup.

html_file = open("AcceptanceSpeeches.html","r") 
links_list = []
# Parse the html file
soup = BeautifulSoup(html_file, 'html.parser')
for x in soup.find_all('a'):
        links_list.append(x.attrs['href'])

#then, another segment needed to loop through HTML <P> tags and extract the speeches

       
url_prefix = 'https://www.oscars.org'
all_text = ''

for link in links_list:
    #link = '/press/91st-oscars-onstage-speech-transcript-music-original-song'
    full_url = url_prefix+link
    #print(full_url)
    page = requests.get(full_url , proxies = {'https':'http://genproxy:8080'},verify=False)
    page_soup = BeautifulSoup(page.content, 'html.parser')
    ps = page_soup.find_all('p')
    for x in ps:
            all_text += str(x)
    #break
    
text_file = open("Output.txt", "w")
text_file.write(all_text)
text_file.close()

#More data cleansing needed to remove stop words, punctuation and extra characters, and Word Cloud is ready!
#https://www.linkedin.com/feed/update/urn:li:activity:6506473887272828928
