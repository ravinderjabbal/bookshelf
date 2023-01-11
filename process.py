import support_selenium


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
    for website in websites_array:
        for chapter in last_chapters_array:
            if support_selenium.is_new_chapter_available(website, chapter):
                support_selenium.get_latest_chapter(website, chapter)
    pass
