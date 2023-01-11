from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

NCA = True
NCNA = True

def is_new_chapter_available(website, chapter):
    if get_latest_chapter(website, chapter):
        pass
    pass


def get_latest_chapter(website, chapter):

    # open website
    # fetch the number > then the <chapter>
    # if its available , return the NCA, if not : NCNA
    driver.get(website)
    if driver.find_element(By.PARTIAL_LINK_TEXT(chapter)) :
        if driver.find_element((By.PARTIAL_LINK_TEXT(chapter + 1))):
            pass
    driver.close()
    pass

#
# if __name__ == "__main__":
#     get_latest_chapter("http://www.google.com", None)
