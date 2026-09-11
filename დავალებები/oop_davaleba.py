# დავალება — Student კლასი 
# შექმენი კლასი Student, რომელსაც ექნება:
# name — სტუდენტის სახელი
# age — ასაკი
# course — რომელ კურსზეა

# შექმენი მეთოდი show_info(), რომელიც დაბეჭდავს სტუდენტის ინფორმაციას მოცემული ფორმატით:
# Name: Luka
# Age: 20
# Course: Python
# Subject: OOP

# შექმენით მინიმუმ ორი ობიექტი და ორივესთვის ცალ-ცალე დაბეჭდეთ შესაბამისი ატრიბუტის მნიშვნელობებიც და მეთოდიც გამოიძახეთ


# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#     def show_info(self):
#         print(f" Name: {self.name}\n Age: {self.age}\n Course: {self.course}")


# student_1 = Student("luka", "20", "Python")
# student_1.show_info()

# student_2 = Student("Giorgi", "23", "Python")
# student_2.show_info()




# # --------------------------------------------

# დავალება — Book კლასი 📚
# შექმენი კლასი Book, რომელსაც ექნება შემდეგი ატრიბუტები:

# title — წიგნის დასახელება
# author — ავტორი
# year — გამოცემის წელი
# genre — ჟანრი

# მოთხოვნები
# შექმენი Book კლასი და __init__ კონსტრუქტორი.
# შექმენი show_info() მეთოდი, რომელიც დაბეჭდავს წიგნის ყველა ინფორმაციას.
# შექმენი __str__ მეთოდი, რომელიც ობიექტის print()-ის დროს დააბრუნებს ასეთ ტექსტს:
# Book: The Hobbit, Author: J.R.R. Tolkien, Year: 1937, Genre: Fantasy

# შექმენი მინიმუმ ორი Book ობიექტი.
# ორივე ობიექტზე გამოიძახე show_info().
# ორივე ობიექტი პირდაპირ დაბეჭდე print()-ით, რათა შეამოწმო __str__ მუშაობს თუ არა.

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}"
    def show_info(self):
        print(f"Book: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}")


book_1 = Book("The Hobbit", "J.R.R. Tolkien", "1937", "Fantasy")
print(book_1)
book_2 = Book("A Man's Head", "Simenon Georges", "1931", "detective")
print(book_2)

# შენიშვნა: არსებული ფაილი აიტანეთ გითჰაბზე, დამიწერეთ რა ქომანდები და პროცესი ჩაატარეთ და საბოლოო ფაილთან ერთად,
# დავალებაში, ამიტვირთეთ გითჰაბის რეპოზიტორიის ლინკიც.