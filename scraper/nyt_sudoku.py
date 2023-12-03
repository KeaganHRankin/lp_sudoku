"""
Webdriver class that scraps the daily NYT sudoku for any difficulty
and returns it in an array format
"""

# -- Imports --
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import re
import numpy as np


class NYTSudoku:
    """
    A webscraper that scrapes the daily sudoku from the New York Times
    """
    
    # Initialize with the webdriver and link.
    def __init__(self):
        """
        instantiate the path to the webdriver
        and the address of the portal
        """
        # Vars for web
        self.path = "selenium webdriver/chromedriver.exe"
        self.web_address = "https://www.nytimes.com/puzzles/sudoku/"
        self.difficulty = 'medium'
        
        # Vars for storing webscraped data.
        self.sudoku_init = []


    def open_webdriver(self):
        """
        Opens the webdriver to the correct web_address.
        """
        # Open the chrome driver
        self.driver = webdriver.Chrome(self.path)

        # Get the CoA website and print the website title
        self.driver.get(self.web_address+self.difficulty)
        

    def close_webdriver(self, delay=0.5):
        """
        Closes the webdriver after a given time delay
        """
        time.sleep(delay)
        self.driver.quit()
        #print('[Info] driver closed :)')


    def retrieve(self):
        """
        Retrieve and reformat the sudoku.
        """
        # get the entire board
        cells = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'su-board')))
        cells_soup = cells.get_attribute('innerHTML')

        # string parse to get only text entries
        cells_l = re.split('aria-label=|class=', cells_soup)
        cells_l = [c.strip().replace('"','') for c in cells_l]
        c_set = ['1','2','3','4','5','6','7','8','9','empty']
        extracted = [x for x in cells_l if x in set(c_set)]

        # clean
        extracted = [int(x.replace('empty','0')) for x in extracted]

        extracted_r = []
        print("Today's clues:")
        for i in range(9):
            n = []
            for j in range(9):
                n.append(9*i+j)
            
            print(extracted[n[0]:n[8]+1])
            extracted_r.append(extracted[n[0]:n[8]+1])
        
        # return
        return extracted_r

    
    def nyt_pipeline(self):
        # run scraper
        self.open_webdriver()
        retreived = self.retrieve()
        self.close_webdriver()

        return np.array(retreived)