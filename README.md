# qa_python
def test_add_new_book_length_name - проверяем, что книга добавляется, с помощью параметризации проверяю, что если длина названия книги больше 40 символов, книга не добавится. Если название книги 40 символов и меньше, книга добавится

def test_set_book_genre - проверяем, что жанр присвоен книге

def get_book_genre_added_book_has_no_genre - проверяем, что у добавленной книги без жанра нет жанра

def test_get_books_with_specific_genre - проверяем, что выводится список книг(название книги) определенного жанра

def test_get_books_genre - проверяем, что приходит словарь books_genre

def test_get_books_for_children - проверяем, что из списка книг выводятся именно книги для детей 

def test_add_book_in_favorites - проверяем, что книги попадают в избранное

def test_unable_delete_book_from_favorites_with_unknown_name - удаляем книгу с неизвестным именем из списка Избранных, проверяем, что добавленная ранее книга на месте

def test_unable_add_book_in_favorites_with_unknown_name - добавляем книгу в список избранного, без основного добавления, проверяем, что список избранного пуст

def test_unable_add_book_in_favorites_with_repeat_name - проверяем, что добавление книги в избранное не задублировалось

def test_delete_book_from_favorites - проверяем, что книга удаляется из избранного

def test_get_list_of_favorites_books - проверяем, что книги добавились в список избранного и проверяем их количество