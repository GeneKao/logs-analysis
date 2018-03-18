#!/usr/bin/env python3

from psycopg2 import connect


class Reporter:

    def __init__(self, dbname):
        "Initieal function"
        self.db = connect('dbname={}'.format(dbname))
        self.cursor = self.db.cursor()
        print("Connection Successful")

    def __enter__(self):
        return self

    def run_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def write_report(self):
        print(self.run_query("select * from authors;"))

    def __exit__(self, exc_type, exc_value, traceback):
        if self.db:
            self.db.close()
            print("Exiting DB")


if __name__ == '__main__':
    print("This is logs analysis program, analysising...")
    with Reporter("news") as reporter:
        reporter.write_report()
