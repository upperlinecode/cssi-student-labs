class Movie:
    media_type = 'Movie' 
    
    def __init__(self, title, runtime, rating):
        self.title = title   
        self.runtime_mins = runtime
        self.rating = rating
        
    def autoplay(self):
        if (self.runtime_mins<=120) and (self.rating>=9.0):
            return "Up Next: " + self.title
        else:
            return "Search for More Movies"
            

forrest = Movie("Forrest Gump", 144, 8.4)
print forrest.autoplay()

lala = Movie("La La Land", 102, 9.6)
print lala.autoplay()