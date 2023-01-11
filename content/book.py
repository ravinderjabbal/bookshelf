class Book:
    __name = ""
    __author = ""
    __location = ""
    __totalChapters = ""
    __lastReadChapter = ""
    __recentlyAddedChapter = ""
    __lastUpdated = ""
    __isbn = ""
    __language = ""
    __rating = ""

    def __init__(self, name, author,location,totalChapters,
                 lastReadChapter,recentlyAddedChapter,
                 lastUpdated,rating=None,language=None,isbn=None):
        self.__name = name
        self.__author = author
        self.__location = location
        self.__totalChapters = totalChapters
        self.__lastReadChapter = lastReadChapter
        self.__recentlyAddedChapter = recentlyAddedChapter
        self.__lastUpdated = lastUpdated
        self.__rating = rating
        self.__language = language
        self.__isbn = isbn


