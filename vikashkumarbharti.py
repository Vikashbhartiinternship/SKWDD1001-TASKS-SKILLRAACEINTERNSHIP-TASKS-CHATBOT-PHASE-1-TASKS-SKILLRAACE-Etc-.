# TASK 1A:-
# i) please write a program to generate all sentences where subject is in["I","you"] and verb is in ["play","love"] and the other object is in["cricket","ludo"].
subjects=["I","LOVE"]
verbs=["PLAY","LOVE"]
objects=["cricket","ludo"]
for subject in subjects:
    for verb in verbs:
        for object in objects:
            print(subject+""+verb+""+ object)
            
             #  ii) Convert emoji into text in Python - Converting emoticons oremojis into text in Python can be done using thedemoji module. Itis used to accurately remove and replace emojis in text strings
             import demoji
            #  load the emoji library
            demoji.download_codes()
            # your text with emojis
            text_with_emojis="I Love "
            # convert emojis with text
            text_with_emojis =demoji.replace (text_with_emojis,"")
print(text_without_emojis)

# TASK 1B :-
# i)Design a ‘book’ class with title, author, publisher, price and author’sroyalty as instance variables. Provide getter and setter properties forall variables. Also define a method royalty() to calculate royalty amount author can expect to receive the following royalties:10% ofthe retail price on the first 500 copies; 12.5% for the next 1,000 copiessold, then 15% for all further copies sold. Then design a new ‘ebook’class inherited from ‘book’ class. Add ebook format (EPUB, PDF,MOBIetc) as additional instance variable in inherited class. Overrideroyalty() method to deduct GST @12% on ebooks
class Book:
    def __init__(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._author_royalty = 0

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def author_royalty(self):
        return self._author_royalty

    def royalty(self, copies_sold):
        if copies_sold <= 500:
            self._author_royalty = 0.10 * self._price * copies_sold
        elif 500 < copies_sold <= 1500:
            self._author_royalty = (0.10 * 500 * self._price) + (0.125 * self._price * (copies_sold - 500))
        else:
            self._author_royalty = (0.10 * 500 * self._price) + (0.125 * 1000 * self._price) + (0.15 * self._price * (copies_sold - 1500))


class Ebook(Book):
    def __init__(self, title, author, publisher, price, format):
        super().__init__(title, author, publisher, price)
        self._format = format

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        self._format = value

    def royalty(self, copies_sold):
        total_royalty = super().royalty(copies_sold)
        gst = 0.12 * total_royalty
        net_royalty = total_royalty - gst
        return net_royalty


# Example usage:
book1 = Book("Book Title", "Author Name", "Publisher", 25.00)
book1.royalty(700)  # Calculate royalty for 700 copies sold

ebook1 = Ebook("Ebook Title", "Author Name", "Publisher", 15.00, "PDF")
ebook1.royalty(1000)  # Calculate royalty for 1000 copies sold


# ii) Implement simple FLAMES game using Python.
def calculate_flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    combined_length = len(name1) + len(name2)

    flames = ["Friend", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(flames) > 1:
        index = (combined_length % len(flames)) - 1
        if index >= 0:
            flames = flames[index + 1:] + flames[:index]
        else:
            flames = flames[:len(flames) - 1]

    return flames[0]


def main():
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")

    result = calculate_flames(name1, name2)

    print(f"The relationship between {name1} and {name2} is: {result}")


if __name__ == "__main__":
    main()
#  TASKCOMPLETED