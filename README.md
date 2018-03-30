# Udacity Full Stack Web Developer
# Project 3 - Logs Analysis Project

> by Gene Ting-Chun Kao

The goal of this project is to write a **internal reporting tool** 
for a newspaper site to discover what kind of articles the site's reader like. 

This python code connects to [postgresql](https://www.postgresql.org/) database 
and write the report as a output.txt file. 

## Installation

### Requirement

- [VirtualBox](https://www.virtualbox.org/wiki/Downloads). 
(Tested with version 5.2.6 r120293 Qt5.6.3)

- [Vagrant](https://www.vagrantup.com/downloads.html). 
(Tested with 2.0.2)

- Python3 

### To run the code

1. Clone my repo `git clone https://github.com/GeneKao/logs-analysis.git`
2. Move the directory folder `cd logs-analysis` 
3. Install the Vagrant environment by running `vagrant up`. 
4. Log in to the virtual machine `vagrant ssh`. 
5. Download the database file
   [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
   and extract to our project directory. 
6. Load the data to Vagrant VM `psql -d news -f newsdata.sql`. 
7. Generate the report `python3 main.py`. 
8. See the result `cat output.txt`.

### To take a look in the database

1. Go to database `psql -d news`.
2. List all the tables `\dt`.
3. Look at the specific table such as articles `\d articles`. 

## Hightight

The python code follow [PEP8](https://www.python.org/dev/peps/pep-0008/) style,
and [Google Style Python
Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html),
and using object-oriented design for this report generating tool. A class
called **Reporter** contains functions such as **write_report** and
**publish_reports**. To use the Reporter class, you will need to use
keyword "with" so the instance will automatically close the connection after it
finishes its job. Questions and answers are written in the dictionaries so this can
be flexible enough to be extended in the future. 


## Contact
Any suggestion please contact [me](https://github.com/GeneKao).
