#web scraper for restricted pages.
#web scraper for naukri.com


import requests
import pprint
import bs4


url = "https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_key_loc&searchType=adv&keyword=full%20stack%20web%20developer&location=bangalore%2Fbengaluru&pageNo=1&experience=0&k=full%20stack%20web%20developer&l=bangalore%2Fbengaluru&experience=0&seoKey=full-stack-web-developer-jobs-in-bangalore-bengaluru&src=jobsearchDesk&latLong=15.133315_78.5162075"

h = {"appid":"109",
           "systemid":"109"}

def get_jobs(x):
    job_id = 0
    page_content = requests.get(x,headers = h)
    page_data = page_content.json()                                             #when this is print.print() , then it returns a mountain of dictionary content.
#    print(page_data.keys())                                                    #when this is passed, then it prints all the keys i.e, like subheadings.
#    print(page_data['jobDetails'])                                             #this prints all the content in the sub-dictionaries in the 'jobDetails' dictionary.
    for i in page_data['jobDetails']:                                           #this will print the list of job titles and the company names.
        job_id += 1
        soup = bs4.BeautifulSoup(i['jobDescription'],'lxml')
        job_descript = soup.text
#        print(i['title'],i['companyName'])                                      #NOTE: refer the output of previous command(line-18) to recognise the names of the sub-dictionaries.
#        print(job_descript)                                              #this will print job job description for every job.
#        print("\n\n")
        #putting the jobs in different files:
        f = open(str(job_id)+".txt","w")
        f.write(i['title'])
        f.write(i['companyName'])
        f.write(job_descript)
        f.close()
        print(job_id,".txt","     .....downloaded")


get_jobs(url)
