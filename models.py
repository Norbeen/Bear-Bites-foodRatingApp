import os, flask_sqlalchemy, app

# app.app = app modules app variable
app.app.config['SQLALCHEMY_DATABASE_URI']  = os.getenv('DATABASE_URL')
# app.app.config['SQLALCHEMY_DATABASE_URI']  = 'postgresql://uname:pass@localhost/postgres'
db = flask_sqlalchemy.SQLAlchemy(app.app)

# This class is for students posting reviews 

class reviewPost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Ucomment = db.Column(db.String(30))
    Urating = db.Column(db.Integer(300))
    Ucategory = db.Column(db.String(300))
    Ulike= db.Column(db.Integer(300))
    Udislike = db.Column(db.Integer(300))
    Uauthor = db.Column(db.String(300))
    Uimage = db.Column(db.String(300))
    Udate = db.Column(db.String(300))
    
    
    
    def __init__(self, comment, rating, category, like, dislike, author, image, date): 
        self.Ucomment = comment
        self.Urating = rating
        self.Ucategory = category
        self.Ulike = like
        self.Udislike = dislike
        self.Uauthor = author
        self.Udimage = image
        self.Udate = date
        
    def __repr__(self):
        # return '<Message user_name: %s>' % self.user_name
        return "{'food comment':'%s', 'food rating':'%s', 'food category':'%s', 'food like':'%s', 'food dislike':'%s', 'food author':'%s', 'food image':'%s' , 'food date':'%s'}" % (self.Ucomment, self.Urating, self.Ucategory, self.Ulike, self.Udislike, self.Uauthor,self.Uimage , self.Udate)

class menuItem(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Utitle = db.Column(db.String(30))
    Urating = db.Column(db.Integer(300))
    Unutrition = db.Column(db.String(300))
    Ureviews= db.Column(db.Integer(300))
    Utypes = db.Column(db.String(300))
    Ulocation = db.Column(db.String(300))
    Uimage = db.Column(db.String(300))
    
    
    def __init__(self, title, rating, nutrition, reviews, types, location, image): 
        self.Utitle = title
        self.Urating = rating
        self.Unutrition = image
        self.Ureviews = reviews
        self.Utypes = types
        self.Ulocation = location
        self.Uimage = image
        
    def __repr__(self):
        # return '<Message user_name: %s>' % self.user_name
        return "{'food title':'%s', 'food rating':'%s', 'food nutrition':'%s', 'food reviews':'%s', 'food types':'%s', 'food location':'%s', 'food image':'%s'}" % (self.Utitle, self.Urating, self.Unutrition, self.Ureviews, self.Utypes, self.Ulocation,self.Uimage )