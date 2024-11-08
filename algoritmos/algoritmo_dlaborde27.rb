class Book
  def initialize(title, author, genre)
    @title = title
    @author = author
    @genre = genre
  end

  def show_details
    puts "Title: #{@title}, Author: #{@author}, Genre: #{@genre}"
  end
end

class Library
  attr_reader :books
  def initialize(name)
    @name = name
    @books = []
  end

  def add_book(book)
    @books << book
  end

  def show_books
    puts "Books in #{@name} Library:"
    @books.each do |book|
      book.show_details
    end
  end

  def search_by_genre(genre)
    puts "Books in #{@name} Library with genre '#{genre}':"
    @books.each do |book|
      if book.instance_variable_get(:@genre) == genre
        book.show_details
      end
    end
  end

  def search_by_author(author)
    puts "Books in #{@name} Library by author '#{author}':"
    @books.each do |book|
      if book.instance_variable_get(:@author) == author
        book.show_details
      end
    end
  end
end

book1 = Book.new("The Hobbit", "J.R.R. Tolkien", "Fantasy")
book2 = Book.new("1984", "George Orwell", "Dystopian")
book3 = Book.new("The Great Gatsby", "F. Scott Fitzgerald", "Classic")

library = Library.new("Central Library")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.show_books
library.search_by_genre("Fantasy")
library.search_by_genre("Dystopian")
library.search_by_author("George Orwell")
library.search_by_author("J.K. Rowling")