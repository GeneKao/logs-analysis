#!/usr/bin/env python3

from psycopg2 import connect


questions = {
    'Q1': 'What are the most popular three articles of all time?',
    'Q2': 'Who are the most popular article authors of all time?',
    'Q3': 'On which days did more than 1% of requests lead to errors? '
}

answers = {
    'A1': '''
    select * from authors;
    ''',

    'A2': '''
    select * from authors;
    ''',

    'A3': '''
    select * from authors;
    '''
}


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

    def write_report(self, ques, ans):
        print(ques)
        print(self.run_query(ans))

    def __exit__(self, exc_type, exc_value, traceback):
        if self.db:
            self.db.close()
            print("Exiting DB")


if __name__ == '__main__':
    print("This is logs analysis program, analysising...")
    with Reporter("news") as reporter:
        reporter.write_report(questions["Q1"], answers["A1"])
        reporter.write_report(questions["Q2"], answers["A2"])
        reporter.write_report(questions["Q3"], answers["A3"])
