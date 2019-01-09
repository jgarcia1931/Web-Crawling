# Web-Crawling
Web Scrapping Using Selenium

### Problems

When attempting to scrape a site I started off by only using Beautiful Soup but 
I noticed that not all of the data was being pulled. The table that I needed to scrape 
was misssing when I pulled the url data.

What I learned is that Beautiful Soup pulls html data and has trouble reading
Javascrip and CSS heavy websites. So I'm assuming that this is why I could not pull the
table from this particular website.

### Selenium
A work around is using Selenium.
Selenium opens the website with Chrome and then pulls the html information from the Chrome
browser. Finally, I was able to scrape the data.

