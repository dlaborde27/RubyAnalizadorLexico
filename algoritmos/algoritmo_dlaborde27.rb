class Book
  def initialize(title, author, genre, year)
    @title = title
    @year = year
    @author = author
    @genre = genre
  end

  def show_details
    puts "Title: #{@title}, Author: #{@author}, Genre: #{@genre}, Year: #{@year}"
  end

  def matches_genre?(genre)
    @genre == genre
  end

  def matches_author?(author)
    @author === author
  end

  def published_before?(year)
    @year < year
  end

  def published_after?(year)
    @year > year
  end

  def published_same_year?(year)
    @year == year
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
    @books.each(&:show_details)
  end

  def search_by_genre(genre)
    puts "Books in #{@name} Library with genre '#{genre}':"
    @books.each do |book|
      book.show_details if book.matches_genre?(genre)
    end
  end

  def search_by_author(author)
    puts "Books in #{@name} Library by author '#{author}':"
    @books.each do |book|
      book.show_details if book.matches_author?(author)
    end
  end

  def search_by_publication_year(year)
    puts "Books published the same year '#{year}':"
    @books.each do |book|
      book.show_details if book.published_same_year?(year)
    end
  end

  def search_by_year_range(start_year, end_year)
    puts "Books published between #{start_year} and #{end_year}:"
    @books.each do |book|
      comparison = book.published_before?(end_year) && book.published_after?(start_year)
      book.show_details if comparison
    end
  end

  def compare_books(book1, book2)
    comparison = book1.year <=> book2.year
    case comparison
    when -1
      puts "#{book1.title} was published before #{book2.title}."
    when 0
      puts "#{book1.title} and #{book2.title} were published in the same year."
    when 1
      puts "#{book1.title} was published after #{book2.title}."
    end
  end
end

book1 = Book.new("The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937)
book2 = Book.new("1984", "George Orwell", "Dystopian", 1949)
book3 = Book.new("The Great Gatsby", "F. Scott Fitzgerald", "Classic", 1925)

library = Library.new("Central Library")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.show_books
library.search_by_genre("Fantasy")
library.search_by_author("George Orwell")
library.search_by_publication_year(1949)
library.search_by_year_range(1930, 1950)
library.compare_books(book1, book3)