import bs4
import requests
import time
import string

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').content
    soup = bs4.BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all("li", class_='clearfix job-bx wht-shd-bx')
    
    # Open a single file to write all job data
    with open('all_jobs.txt', 'w') as f:
        for index, job in enumerate(jobs):
            pub_date = job.find('span', class_='sim-posted').span.text
            if 'Posted' in pub_date:
                job_name = job.find('header', class_='clearfix').h2.text
                company_name = job.find('h3', class_='joblist-comp-name').text.split('\n')[1]
                req_skills = job.find('span', class_='srp-skills').text
                more_info = job.header.h2.a['href']
                
                # Write the job details to the file
                f.write(f'Job {index + 1}:\n')
                f.write(f'Job Name: {job_name.strip()}\n')
                f.write(f'Company Name: {company_name.strip()}\n')
                f.write(f'Required Skills: {req_skills.strip()}\n')
                f.write(f'For more information, visit: {more_info}\n')
                f.write('\n' + '-'*40 + '\n\n')  # Separate each job with a line
        print('All job data has been saved to "all_jobs.txt"')

find_jobs()

