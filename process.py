import save_data
import support_selenium
from ui_code import refresh_ui
from datetime import date


def processing_data(data):
    data_array = data.to_numpy()
    print("Data in array = ", data_array)
    print("Len = ", len(data_array))
    websites_array = all_websites(data_array)
    chapters_array = all_chapters(data_array)
    update_details(websites_array, chapters_array)
    return None


def all_websites(data_array):
    websites = []
    for row in range(len(data_array)):
        for column in range(0, 9):
            if column == 8:
                websites.append(data_array[row][column])
    print(websites)
    return websites


def all_chapters(data_array):
    chapters = []
    for row in range(len(data_array)):
        for column in range(0, 5):
            if column == 4:
                chapters.append(data_array[row][column])
    print(chapters)
    return chapters


def update_details(websites_array, last_chapters_array):
    for i in range(0, len(websites_array)):
        latest_chapter = support_selenium.is_new_chapter_available(websites_array[i], last_chapters_array[i])
        if latest_chapter:
            today_date = date.today()
            save_data.update_data(websites_array[i], last_chapters_array[i] + 1, today_date)
    support_selenium.tear_down()
    refresh_ui()
    pass
