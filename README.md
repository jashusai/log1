# Logs Analysis Project:

Building an informative summary from logs by sql database queries. Interacting with a live database both from the command line and from the python code.

## Software Technologies used:

1.PostgreSQL

2.Writing Python code with DB-API

3.Virtual machine (VM) Vagrant

## Project Requirements:

Reporting tool should answer the following questions:

1.Most popular three articles of all time

2.Most popular authors of all time

3.On which days did more than 1% of requests lead to errors?

Project follows good SQL coding practices:

1.Each question should be answered with a single database query.

2.The code is error free and conforms to the PEP8 style recommendations.

3.The code presents its output in clearly formatted plain text.

## Setup environment:

1.Download Vagrant and install.

2.Download Virtual Box and install.

3.Download newsdata.sql file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
  
## Run these commands from the terminal in the folder where your vagrant is installed in:

1.open the terminal.

2.Navigate to the folder with the project files which includes (1. news.py, 2. newsdata.sql)

3.Ensure the Vagrant File configuration has been downloaded to.

4.run the virtual machine with command vagrant up then vagrant ssh.

5.once inside the VM,postgresql and psycopg2 are installed.

6.load the database by running psql -d news -f newsdata.sql

7.cd /vagrant to change to your vagrant directory.

8.python news.py to run the reporting tool.
