#!/usr/bin/env python3

"""This is the main code to analyse

Example:
    To run this code using python3 on the console,
    and this will generate output.txt file as report.

        $ python3 main.py

"""

__author__ = "Gene Ting-Chun Kao"
__email__ = "kao.gene@gmail.com"

from psycopg2 import connect


# Questions dictionary
questions = {
    'Q1': 'What are the most popular three articles of all time?',
    'Q2': 'Who are the most popular article authors of all time?',
    'Q3': 'On which days did more than 1% of requests lead to errors? '
}


# Question types are used for formatting different answers
question_types = {'Q1': 'A', 'Q2': 'A', 'Q3': 'B'}


# Answers query dictionary
answers = {
    'A1': '''
        select articles.title, count(*) as num
        from articles, log
        where log.status like '%200%'
        and articles.slug = substring(log.path, 10)
        group by articles.title
        order by num desc
        limit 3;
    ''',

    'A2': '''
        select authors.name, count(*) as num
        from articles, authors, log
        where log.status like '%200%'
        and articles.slug = substring(log.path, 10)
        and authors.id = articles.author
        group by authors.name
        order by num desc;
    ''',

    'A3': '''
        select * from
        (select date(time) as day,
        round(sum(case when status like '%404%' then 1 else 0 end)
        * 100.0 / count(*), 1) as error
        from log
        group by day) as view
        where error > 1.0;
    '''
}


class Reporter(object):
    """Class as a news reporter, give it questions and answers to write report

    Attributes:
       file_name (str): output file name
       _db (obj): database object
       _cursor (obj): cursor from database
    """

    def __init__(self, db_name, output_file):
        """Initial function, connect to db.

        Args:
           db_name (str): the name of the databases to connect.
           output_file (str): output file name

        """
        self.file_name = output_file
        self._db = connect('dbname={}'.format(db_name))
        self._cursor = self._db.cursor()
        print("Connection Successful")

    def __enter__(self):
        return self

    def _run_query(self, query):
        """Run input query

        Note:
            This is the method to execute the query.

        Args:
            query (str): postgresql query string.

        Returns:
            (str): Qeury result in string
        """
        self._cursor.execute(query)
        return self._cursor.fetchall()

    def _prepare_report(self):
        """Clean up the file before writing report"""
        file = open(self.file_name, "w")
        file.write("")
        file.close()

    def _write_report(self, ques, ques_type, ans, num):
        """Print out the report

        Args:
            ques (str): Question
            ques_type (str): question types for format
            ans (str): Answers
            num (int): index number of this report
        """
        print(self._run_query(ans))
        results = self._run_query(ans)

        file = open(self.file_name, "a")

        # Write question title
        file.write(str(num) + ". " + ques + "\n")

        # Write answers, here we have two type of questions,
        # this is extendable with more types of Q&A in the future.
        if (ques_type == "A"):
            for result in results:
                file.write(
                    "  • \"" + result[0] + "\" — "
                    + str(result[1]) + " views" + "\n")
        elif (ques_type == "B"):
            for result in results:
                file.write(
                    "  • \"" + str(result[0]) + "\" - "
                    + str(result[1]) + "% errors")

        file.write("\n")
        file.close()

    def publish_reports(self, questions, question_types, answers):
        """Publish the report

        Args:
            questions (:list: str): A list of questions
            question_types (:list: str) A list of quesiton types
            answers (:list: str): A list of answers
        """
        self._prepare_report()  # Clean up file first

        # Loop through different questions and answers
        for i in range(len(questions)):
            i += 1
            self._write_report(
                questions["Q{}".format(i)],
                question_types["Q{}".format(i)],
                answers["A{}".format(i)], i)
        print("All questions and answers are successfully writen to file")

    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the db"""
        if self._db:
            self._db.close()
            print("Exiting DB")


if __name__ == '__main__':
    print("This is logs analysis program, analysising...")
    with Reporter("news", "output.txt") as reporter:
        reporter.publish_reports(questions, question_types, answers)
