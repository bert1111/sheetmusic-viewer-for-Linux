from kivy.event import EventDispatcher
from kivy.properties import NumericProperty

class PageNavigator(EventDispatcher):
    current_page = NumericProperty(0)
    total_pages = NumericProperty(0)

    def set_total_pages(self, total):
        self.total_pages = total
        self.current_page = 0

    def next_page(self):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
        return self.current_page

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
        return self.current_page
