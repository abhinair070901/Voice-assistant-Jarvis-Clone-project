from selenium import webdriver

class infow():
    def __init__(self):
        self.driver = webdriver.chrome(executable_path='C:\Users\user\Desktop\chromedriver_win32')

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')#triggers the search box stores in search variable
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()#the query is searched.
