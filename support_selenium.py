from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
# Added add blocker extension
chrome_extension_file = "/Users/30153/Documents/bookshelf/bookshelf/AdGuard-AdBlocker.crx"
chrome_options.add_extension(chrome_extension_file)
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)


def is_new_chapter_available(website, last_recorded_chapter):
    next_chapter = last_recorded_chapter + 1
    new_chapter = ""
    driver.get(website)
    is_last_chapter_present = driver.find_element_by_partial_link_text(str(last_recorded_chapter)).text
    is_next_chapter_present = driver.find_element_by_partial_link_text(str(next_chapter)).text
    if is_last_chapter_present:
        if is_next_chapter_present:
            for i in is_next_chapter_present:
                if i.isdigit():
                    new_chapter += i
            return True
    return False


def get_latest_chapter(website, last_recorded_chapter):
    # open website
    # fetch the number > then the <last_recorded_chapter>
    # if its available , return the True
    driver.get(website)
    next_chapter = last_recorded_chapter + 1
    pass


def tear_down():
    print("Teared Down")
    driver.close()
#
# if __name__ == "__main__":
#     get_latest_chapter("http://www.google.com", None)
