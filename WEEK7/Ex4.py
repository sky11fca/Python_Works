class Library:
    def __init__(self, title_list):
        self.title_list = list(set(title_list))

    def add_books(self, new_list):
        self.title_list = list(set(self.title_list + new_list))

    def remove_book(self, title):
        if title not in self.title_list:
            return None
        self.title_list.remove(title)
        return self.title_list
    def statistics(self):
        print(len(self.title_list), sorted(self.title_list))
    def __str__(self):
        string_result = []

        for idx in range(len(self.title_list)-1):
            string_result.append(f"{self.title_list[idx]}, ")

        string_result.append(f"{self.title_list[len(self.title_list)-1]}")
        return "".join(string_result)

library = Library(["The Hobbit", "The Fellowship of the Ring", "The Two Towers"])
library.add_books(["The Return of the King", "The Hobbit: An Unfinished Story"])
library.remove_book("The Hobbit")
library.statistics()
print(library)