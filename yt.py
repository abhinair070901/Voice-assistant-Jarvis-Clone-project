from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.chrome(executable_path='C:\Users\user\Desktop\chromedriver_win32')

    def play(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element_by_xpath('//*[@id="dismissable"]')
        video.click()
       
#assist=music()
#assist.play()