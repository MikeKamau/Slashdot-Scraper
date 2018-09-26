SLASHDOT ARTICLE TITLE AND VIEWS SCRAPER
========================================
A simple Scrapy framework crawler that crawls through slashtdot.org and retrives all story titles together with their associated comment numbers, and stores them in a MySQL db.

PREREQUISITES
================
This project was created using Scrapy 1.5.1 ,Python 3.6.6 and MySQL 5.7.23.
Anaconda was used for package management and you can install all the project dependencies using the provided requirements.txt file, provided with the project.
You'll also need to create a database named "slashdot" and within in create a table called "stories".

#MySQL Syntax:
#Create slashdot database
create database slashdot;

#Create stories table
CREATE TABLE `stories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `comments` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

Whnen everything is set up be sure to change MySQL values for "host", "user" and "password" to the appropriate values according to your environment, in the "pipelines.py" file.

RUNNING THE CRAWLER
====================
Once you cloned the repository onto your machine, run the following command to run the crawler:

scrapy crawl easy
