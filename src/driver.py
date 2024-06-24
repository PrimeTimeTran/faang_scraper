import re
import time
import statistics

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class Driver:
    def __init__(self) -> None:
        super().__init__()
        chrome_driver_path = '/usr/local/bin/chromedriver'
        service = Service(executable_path=chrome_driver_path)
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(service=service, options=options)

    def load_page_source(self, url, timeout = 10):
        self.driver.get(url)
        time.sleep(timeout)
        return self.driver.page_source

    def search_element_in_file(self, file, start_term, end_term=None):
        try:
            with open(file, 'r', encoding='utf-8') as file:
                page_content = file.read()
                soup = BeautifulSoup(page_content, 'html.parser')
                if end_term:
                    elements = soup.find_all(text=lambda text: isinstance(text, str) and text.strip().startswith(start_term) and text.strip().endswith(end_term))
                else:
                    elements = soup.find_all(text=lambda text: isinstance(text, str) and text.strip().startswith(start_term))
                return elements
        except FileNotFoundError:
            print(f"File '{file}' not found.")
        except Exception as e:
            print(f'Error: search_element_in_file {e}')
        finally:
            pass
    
    def target_main_content(self, page_content):
        try:
            soup = BeautifulSoup(page_content, 'html.parser')
            h1_element = soup.find('h1', string="Search Jobs")
            if h1_element:
                next_div_sibling = h1_element.find_next_sibling('div')
                if next_div_sibling:
                    main = next_div_sibling.find('main')
                    if main:
                        return next_div_sibling.find('main')
        except Exception as e:
            print(f'Error: target_main_content {e}')

    def find_elements_containing_text(self, content, tag, text):
        soup = BeautifulSoup(content, 'html.parser')
        return soup.find_all(tag, string=lambda s: text in s if s else False)

    def extract_numbers(self, strings):
        numbers = []
        for string in strings:
            found_numbers = re.findall(r'\d+\.?\d*', string)
            numbers.extend([float(num) for num in found_numbers])
        return numbers

    def calculate_average(self, numbers):
        if numbers:
            return statistics.mean(numbers)
        else:
            return 0

    def clean(self, lst):
        return list(filter(None, [li.text.strip() for li in lst]))