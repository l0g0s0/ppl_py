import unittest
from book import Book
from book_manager import BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

    def test_add_book(self):
        """Test menambahkan buku"""
        book = Book("Pemrograman", "Andi", 2020)
        self.book_manager.add_book(book)
        self.assertEqual(1, len(self.book_manager.get_all_books()))

    def test_remove_existing_book(self):
        """Test menghapus buku yang ada"""
        book = Book("Basis Data", "Erlangga", 2021)
        self.book_manager.add_book(book)

        removed = self.book_manager.remove_book("Basis Data")
        self.assertTrue(removed)
        self.assertEqual(0, len(self.book_manager.get_all_books()))

    def test_remove_non_existing_book(self):
        """Test menghapus buku yang tidak ada"""
        removed = self.book_manager.remove_book("Tidak Ada")
        self.assertFalse(removed)
        self.assertEqual(0, len(self.book_manager.get_all_books()))

    def test_find_books_by_author(self):
        """Test mencari buku berdasarkan author"""
        book1 = Book("Python Dasar", "Andi", 2020)
        book2 = Book("Java Lanjutan", "Budi", 2021)
        book3 = Book("AI Modern", "Andi", 2022)

        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)
        self.book_manager.add_book(book3)

        result = self.book_manager.find_books_by_author("Andi")
        self.assertEqual(2, len(result))
        self.assertIn(book1, result)
        self.assertIn(book3, result)

    def test_find_books_by_year(self):
        """Test mencari buku berdasarkan tahun"""
        book1 = Book("Python Dasar", "Andi", 2020)
        book2 = Book("Java Lanjutan", "Budi", 2021)

        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)

        result = self.book_manager.find_books_by_year(2020)
        self.assertEqual(1, len(result))
        self.assertIn(book1, result)

    def test_find_books_by_title(self):
        """Test mencari buku berdasarkan judul"""
        book = Book("Python Dasar", "Andi", 2020)
        self.book_manager.add_book(book)

        self.assertTrue(self.book_manager.find_books_by_title("Python Dasar"))
        self.assertFalse(self.book_manager.find_books_by_title("Tidak Ada"))

    def test_get_all_books(self):
        """Test mendapatkan semua buku"""
        book1 = Book("Python Dasar", "Andi", 2020)
        book2 = Book("Java Lanjutan", "Budi", 2021)

        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)

        result = self.book_manager.get_all_books()
        self.assertEqual(2, len(result))
        self.assertIn(book1, result)
        self.assertIn(book2, result)

    def test_clear_all_books(self):
        """Test menghapus semua buku"""
        book1 = Book("Python Dasar", "Andi", 2020)
        book2 = Book("Java Lanjutan", "Budi", 2021)

        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)

        self.book_manager.clear_all_books()
        self.assertEqual(0, len(self.book_manager.get_all_books()))

if __name__ == '__main__':
    unittest.main()
