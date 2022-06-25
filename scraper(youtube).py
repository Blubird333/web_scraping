# web scraping
#This code will show the job info refreshing 5 times with an interval of 30 secs.

import bs4
import requests
import time
import string

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').content
    soup = bs4.BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all("li",class_ = 'clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        pub_date = job.find('span',class_ = 'sim-posted').span.text
        if 'Posted' in pub_date:
            job_name = job.find('header',class_ = 'clearfix').h2.text
            company_name = job.find('h3',class_ = 'joblist-comp-name').text.split('\n')[1]
            req_skills = job.find('span',class_ = 'srp-skills').text
            more_info = job.header.h2.a['href']
            fname = str(index)+'.txt'
            with open(fname,'w') as f:
                f.write(f'Job Name: {job_name.strip()}\n\n')
                f.write(f'Company Name: {company_name.strip()}\n\n')
                f.write(f'Required Skills: {req_skills.strip()}\n\n')
                f.write(f'For more information, visit "{more_info}"')
                f.close()
            print(f'Saved as file: {index}.txt')
find_jobs()

#if __name__ == '__main__':
#    i=0
#    while i<5:
#        find_jobs()
#        time_gap = 10
#        print("waiting ...")
#        i+=1
#        time.sleep(time_gap*3)
