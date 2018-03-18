from website.lib.database import Database


class Threads:
    database = None

    def __init__(self):
        if self.database is None:
            self.database = Database()

    def create_new_thread(self, thread, created_date):
        self.database.insert_thread(thread, created_date)
