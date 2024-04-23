import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        books_collector = BooksCollector()

        books_collector.add_new_book('Гордость и предубеждение и зомби')
        books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(books_collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    #
    @pytest.mark.parametrize(
        'name, expected_result',
        [
            ['X', True],
            ['Lorem ipsum dolor sit amet, consectet 40', True],
            ['Lorem ipsum dolor sit amet, consectetuer > 40', False],
        ]
    )
    def test_add_new_book_length_name(self, name, expected_result):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        actual_result = books_collector.get_book_genre(name) is not None
        assert actual_result == expected_result

    def test_add_book_added_book_has_no_genre(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Война и мир')
        assert books_collector.get_book_genre('Война и мир') == ''

    # def test_set_book_genre(self):
    #     books_collector = BooksCollector()
    #     name = 'Гарри Поттер и принц полукровка'
    #     genre = 'Фантастика'
    #     books_collector.add_new_book(name)
    #     books_collector.set_book_genre(name, genre)
    #     assert books_collector.set_book_genre(name, genre) == genre

    def test_get_book_genre(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Гарри Поттер и принц полукровка')
        books_collector.set_book_genre('Гарри Поттер и принц полукровка', 'Фантастика')
        assert books_collector.get_book_genre('Гарри Поттер и принц полукровка') == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Азазель')
        books_collector.set_book_genre('Азазель', 'Детектив')
        books_collector.add_new_book('Ночь в Люберцах')
        books_collector.set_book_genre('Ночь в Люберцах', 'Ужасы')
        assert books_collector.get_books_with_specific_genre('Ужасы') == ['Ночь в Люберцах']

    def test_get_books_for_children(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Чик и Брики')
        books_collector.set_book_genre('Чик и Брики', 'Мультфильмы')
        books_collector.add_new_book('Азазель')
        books_collector.set_book_genre('Азазель', 'Детектив')
        assert books_collector.get_books_for_children() == ['Чик и Брики']

    def test_add_book_in_favorites(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Гарри Поттер и принц полукровка')
        books_collector.add_book_in_favorites('Гарри Поттер и принц полукровка')
        assert books_collector.get_list_of_favorites_books() == ['Гарри Поттер и принц полукровка']

    def test_get_list_of_favorites_books(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Гарри Поттер и принц полукровка')
        books_collector.add_new_book('Гарри Поттер и дары смерти')
        books_collector.add_book_in_favorites('Гарри Поттер и принц полукровка')
        books_collector.add_book_in_favorites('Гарри Поттер и дары смерти')
        assert len(books_collector.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Гарри Поттер и принц полукровка')
        books_collector.add_book_in_favorites('Гарри Поттер и принц полукровка')
        books_collector.delete_book_from_favorites('Гарри Поттер и принц полукровка')
        assert books_collector.get_list_of_favorites_books() == []
