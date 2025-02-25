# Article class to manage articles with immutable title and relationships
class Article:
    # Class variable to track all articles
    all = []

    def __init__(self, author, magazine, title):
        # Store title as private attribute to make it immutable
        self._title = title
        self.author = author
        self.magazine = magazine
        # Add article to class-level tracking
        Article.all.append(self)

    # Property decorator to make title read-only
    @property
    def title(self):
        return self._title

    # Setter that ignores changes to maintain immutability
    @title.setter
    def title(self, value):
        # Title is immutable, so we ignore any attempts to change it
        pass

# Author class to manage authors and their relationships
class Author:
    def __init__(self, name):
        # Store name as private attribute to make it immutable
        self._name = name

    # Property decorator to make name read-only
    @property
    def name(self):
        return self._name

    # Setter that ignores changes to maintain immutability
    @name.setter
    def name(self, value):
        # Name is immutable, so we ignore any attempts to change it
        pass

    # Get all articles by this author
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # Get unique magazines this author has written for
    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    # Create new article with this author
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    # Get unique categories of magazines written for
    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))

# Magazine class to manage magazines with mutable properties
class Magazine:
    def __init__(self, name, category):
        # Store as private attributes but allow mutation with validation
        self._name = name
        self._category = category

    # Property with validation in setter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Only update if valid string between 2-16 chars
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        # Only update if valid non-empty string
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    # Get all articles in this magazine
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # Get unique authors who have written for this magazine
    def contributors(self):
        return list(set(article.author for article in self.articles()))

    # Get list of article titles or None if empty
    def article_titles(self):
        articles = self.articles()
        return [article.title for article in articles] if articles else None

    # Get authors with more than 2 articles in this magazine
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1

        authors = [author for author, count in author_counts.items() if count > 2]
        return authors if authors else None