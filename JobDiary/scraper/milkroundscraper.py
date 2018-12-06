import urllib.request
from bs4 import BeautifulSoup
from JobDiary.scraper import dictionary


class MilkroundScraper:

    def __init__(self, url):
        page = urllib.request.urlopen(url)
        self.soup = BeautifulSoup(page, 'html.parser')

    def get_credentials(self):
        return [self.get_title(),
                self.get_company_name(),
                self.get_salary(),
                self.get_type(),
                self.get_location(),
                self.get_grade()]

    def get_title(self):

        job_title = self.soup.find('h1', attrs={'class': 'brand-font'})

        return " ".join(job_title.text.split()).split(":")[0].split(",")[0]

    def get_salary(self):

        for div in self.soup.find_all('li', attrs={'class': 'salary icon'}):

            return " ".join(div.text.split()).split("+")[0]

    def get_company_name(self):
        company_name = self.soup.find('a', attrs={'id': 'companyJobsLink'})

        return " ".join(company_name.text.split())

    def get_location(self):
        location = self.soup.find('li', attrs={'class': 'location icon'})

        if location is None:
            location = self.soup.find('div', attrs={'class': 'col-xs-12 col-md-10 travelTime-container'})

        return " ".join(location.text.split()).split(",")[0]

    def get_type(self):
        location = self.soup.find('li', attrs={'class': 'job-type icon'})

        return " ".join(location.text.split())

    def get_grade(self):
        for element in self.soup.find_all():
            return dictionary.check_grade(element.text.lower())



