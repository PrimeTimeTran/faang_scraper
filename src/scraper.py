import os
import time
import math
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

from .logger import Log
from .driver import Driver

from .utils import dl_dir
from .constants import urls, company_specific

# [x] 0. Loop through all search term pages
# [x] 1. Calculate how many pages there are for each search term.
# [x] 2. Download each index page
# [x] 3. Download all show pages
# [ ] MS
# [ ] Meta
# [ ] Apple
# [ ] Amazon
# [ ] Netflix
# [ ] Nvidia
# [x] Google

class Scraper(Driver, Log):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.roles = ['se', 'data', 'ai', 'ml']
        self.companies = ['google']
        self.company_page_map = {}
        # current_date = datetime.now()
        # formatted_date = current_date.strftime("%Y-%m")
        # self.period = formatted_date

    def start_entire_thing(self):
        # self.dl_all()
        self.parse_company_summaries()
        self.dl_role_index_pages()
        self.parse_show_pages()
        self.dl_show_pages()
        self.parse_show_pages()

    def write_summaries_to_csv(self):
        try:
            self.log('write_summaries_to_csv')
            df = pd.DataFrame()
            for company in self.companies:
                csv_file = f'{dl_dir}/{self.period}_{company}_summary.csv'
                total_roles = 0
                new_data = {
                    'period': [self.period],
                    'company': [company]
                }
                for role in self.roles:
                    total_items = self.company_page_map[f'{company}-{role}']
                    new_data[role] = total_items
                    page_count = int(
                        self.company_page_map[f'{company}-{role}-page_count'])
                    new_data[f'{role}_pages'] = page_count
                    total_roles += total_items
                new_data['total'] = total_roles
                df_new = pd.DataFrame(new_data)
                columns_to_convert = ['se_pages',
                                      'data_pages', 'ai_pages', 'ml_pages']
                df_new[columns_to_convert] = df_new[columns_to_convert].astype(
                    int)
                df = pd.concat([df, df_new], ignore_index=True)
                df.to_csv(csv_file, index=False)
        except Exception as e:
            self.log(f'An exception occurred: {str(e)}')

        self.log(f"Data appended and written back to {csv_file}.")

    def write_links_to_csv(self, links, company, role):
        self.log('write_links_to_csv')
        csv_file = f'{dl_dir}{self.period}_{company}_job_links.csv'
        df = pd.read_csv(csv_file)
        for link in links:
            new_data = {
                'period': [self.period],
                'company': [company],
                'role': [role],
                'link': [link],
            }
            df_new = pd.DataFrame(new_data)
            df = pd.concat([df, df_new], ignore_index=True)
            df.to_csv(csv_file, index=False)

        self.log(f"Data appended and written back to {csv_file}.")

    def dl_all(self):
        for company in self.companies:
            for role in self.roles:
                url = urls[company][role]
                content = self.load_page_source(url)
                current_date = datetime.now()
                formatted_date = current_date.strftime("%Y-%m")
                filename = f"{dl_dir}{company}/{formatted_date}_{company}_{role}_0.html"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.log(f"File downloaded: {filename}")
                time.sleep(2)

    def parse_company_summaries(self):
        try:
            for company in self.companies:
                for role in self.roles:
                    self.log(f'Calculating # pages of {company}: {role}')
                    file = f"{dl_dir}{company}/{self.period}_{company}_{role}_0.html"
                    start = urls[f'{company}_start_key']
                    end = urls[f'{company}_end_key']
                    elements = self.search_element_in_file(file, start, end)
                    if company == 'ms':
                        # Wont work. Individual jobs need to be clicked to SPA load the next page. Need a driver to handle"
                        second = elements[0].split('of')[1]
                        total_items = int(second.split(' ')[1])
                        num_pages = math.ceil(total_items / 20)
                        self.company_page_map[f'{company}-{role}'] = total_items
                        self.company_page_map[f'{company}-{role}-page_count'] = num_pages
                    elif company == 'google':
                        selected_items = [
                            item for item in elements if "20 of " in item]
                        total_items = int(selected_items[0].split(' ')[-1])
                        num_pages = math.ceil(total_items / 20)
                        self.company_page_map[f'{company}-{role}'] = total_items
                        self.company_page_map[f'{company}-{role}-page_count'] = num_pages
                    elif company == 'meta':
                        self.log(
                            'No Query param for page. Need to click through pages.')
            self.log(self.company_page_map)
            self.write_summaries_to_csv()
        except:
            self.log('An exception occurred: parse_company_summaries')

    def dl_role_index_pages(self):
        try:
            for company in self.companies:
                for role in self.roles:
                    for i in range(1, self.company_page_map[f'{company}-{role}']+1):
                        self.log(f'Download pages of {company}: {role}, {i}')
                        base_url = urls[company][role]
                        page = f"{company_specific[company]['page_name']}={i}"
                        url = f'{base_url}&{page}'
                        content = self.load_page_source(url)
                        filename = f"{dl_dir}{company}/{self.period}_{company}_{role}_{i}.html"
                        with open(filename, 'w', encoding='utf-8') as f:
                            self.log(f"File downloaded: {filename}")
                            f.write(content)
        except:
            self.log('An exception occurred: dl_role_index_pages')

    def parse_show_pages(self):
        try:
            self.log('parse_show_pages')
            for company in self.companies:
                filename = f'{dl_dir}{self.period}_{company}_summary.csv'
                df = pd.read_csv(filename)
                row = df.iloc[0]
                for role in self.roles:
                    length = row[f'{role}_pages']
                    self.log(f'{company}-{role}')
                    for i in range(1, length + 1):
                        links = []
                        file = f"{dl_dir}{company}/{self.period}_{company}_{role}_{i}.html"
                        with open(file, 'r', encoding='utf-8') as f:
                            content = f.read()
                            ul_children = []
                            c_wiz = self.target_main_content(content)
                            if c_wiz:
                                ul_element = c_wiz.find('ul')
                                if ul_element:
                                    ul_children = c_wiz.find_all(
                                        recursive=False)[0]
                                else:
                                    self.log(
                                        "No ul element found within the next div sibling of the h1 element.")
                            else:
                                self.log("No C-Wiz.")
                            job_items = ul_children.find_all(
                                'li', class_='lLd3Je')
                            for el in job_items:
                                link_elem = el.find(
                                    'a', href=lambda href: href and href.startswith('jobs/results'))
                                if link_elem:
                                    link = link_elem['href']
                                    full_link = f'https://www.google.com/about/careers/applications/{link}'.split('?')[
                                        0]
                                    links.append(full_link)
                        self.write_links_to_csv(links, company, role)
        except:
            self.log('An exception occurred: parse_show_pages')

    def dl_show_pages(self):
        self.log('dl_show_pages')
        company = 'google'
        try:
            filename = f'{dl_dir}/{self.period}_{company}_job_links.csv'
            df = pd.read_csv(filename)
            for idx, row in df.iterrows():
                role = row[2]
                link = row[3]
                content = self.load_page_source(link, 5)
                name = f"{dl_dir}{company}/{self.period}_{role}_{idx}.html"
                with open(name, 'w', encoding='utf-8') as f:
                    self.log(f"File downloaded: {name}")
                    f.write(content)
                    df.at[idx, 'filename'] = name
                df.to_csv(filename, index=False)
        except:
            self.log('An exception occurred: fix_csvs')

    def parse_show_pages(self):
        try:
            self.log('parse_show_pages')
            for _, company in enumerate(self.companies):
                parsed_jds = f'{dl_dir}{self.period}_{company}_jobs.csv'
                if os.path.exists(parsed_jds):
                    df = pd.read_csv(parsed_jds)
                else:
                    df = pd.DataFrame(columns=['period', 'title'])

                job_links_file = f'{dl_dir}{self.period}_{company}_job_links.csv'
                df_links = pd.read_csv(job_links_file)
                for idx, row in df_links.iterrows():
                    if idx == 1: break
                    self.log(row)
                    filename = row[4]
                    with open(filename, 'r', encoding='utf-8') as f:
                        content = f.read()
                        soup = BeautifulSoup(content, 'html.parser')
                        main = soup.find('main')
                        title = main.find_all('h2')[0].text
                        degree = main.find_all('li')
                        degree = degree[4:][0].text
                        experiences = self.find_elements_containing_text(
                            content, 'li', 'years of')
                        experiences = [li.text for li in experiences]
                        nums = self.extract_numbers(experiences)
                        experience = self.calculate_average(nums)
                        h3 = main.find_all('h3')

                        minimum = h3[0].next_sibling
                        preferred = h3[1].next_sibling
                        responsibilities = h3[3].next_sibling

                        min_texts = self.clean(minimum)
                        preferred_texts = self.clean(preferred)
                        responsibilities_texts = self.clean(responsibilities)

                        new_data = {
                            'period': [self.period],
                            'title': [title],
                            'degree': [degree.replace('\n', '')],
                            'experience': [experience],
                            'minimum': [min_texts],
                            'preferred': [preferred_texts],
                            'responsibilities': [responsibilities_texts],
                        }

                        df_new = pd.DataFrame(new_data)
                        df = pd.concat([df, df_new], ignore_index=True)

                        df.to_csv(parsed_jds, index=False)
        except:
            self.log('An exception occurred: parse_show_pages')

    def fix(self):
        try:
            filename = f'{dl_dir}/{self.period}_google_job_links.csv'
            df = pd.read_csv(filename)
            df.insert(0, 'period', self.period)
            df.to_csv(filename, index=False)
        except:
            self.log('An exception occurred: fix_csvs')
