#import beautifulsoup and request her
import requests
from bs4 import BeautifulSoup
import json



def displayJobDetails(jobDetails):
    print("Display job details")
    print(jobDetails)

#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role,location):

    jobList = {}

    url = 'https://www.indeed.com/jobs?q=' + role + '&l=' + location

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    jobList["title"] = soup.find('h2', class_= 'jobTitle').text
    jobList["company"] = soup.find('span', class_= 'companyName').text
    jobList["description"] = soup.find('div', class_= 'job-snippet').text
    jobList["salary"] = soup.find('div', class_= 'salary-snippet-container').text

    return jobList

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")
    with open("jobDetails.json", "w") as outfile:
        json.dump(jobDetails, outfile)

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter the location you want to search")
    location = input()
    print("Enter role you want to search")
    role = input()
    print("The location you have entered is " + location + " and the role you have entered is " + role)
    # Complete the missing part of this function here
    jobList = getJobList(role,location)
    displayJobDetails(jobList)
    saveDataInJSON(jobList)

if __name__ == '__main__':
    main()