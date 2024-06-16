class Article:
    
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
        
    @property
    def title(self):
       return self._title
   
   
    @title.setter
    def title(self, title):
       if type(title) in (str,) and (5<=len(title)<=50) and (hasattr(self, title)==False):
           self._title = title
    #    else:
    #        raise Exception("Invalid title")
 
   
class Author:
    def __init__(self, name):
        self.name = name 


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) in (str,) and (len(name)) and (hasattr(self, "name")==False):
            self._name = name
        # else:
        #     raise Exception("Invalid name")
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
        
    def magazines(self):
        return list(set(article.magazine for article in self.articles()))
        
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
       

    def topic_areas(self):
        topics = (set(magazine.category for magazine in self.magazines()))
        if len(topics) == 0:
            return None
        else:
            return list(topics)

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        # self._validate_name(name)


    @property
    def name(self):
        return self._name
    
    
    @name.setter
    def name(self, name):
        if type(name) in (str,) and (2<=len(name)<=16):
            self._name = name
        # else:
        #     raise Exception("Invalid name")
            
    
    @property
    def category(self):
        return self._category
    
    
    @category.setter
    def category(self, category):
        if type(category) in (str,) and len(category)>0:
            self._category = category
        # else:
        #     raise Exception("Invalid category")
        
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        if len(titles) == 0:
            return None
        else:
            return titles

    def contributing_authors(self):
        authors = (set(article.author for article in self.articles()))
        moreThanTwoArticles = [author for author in authors if sum(1 for article in self.articles() if article.author == author) > 2]
        if len(moreThanTwoArticles) == 0:
            return None
        else:
            return moreThanTwoArticles
        