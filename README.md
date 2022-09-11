# Amazon-Price-Monitor

This is a price monitor program that checks the price of a product on amazon, it compares the pice with your target price and alerts you with an 
email if the price of the product is less or equal to your target price.

This program takes the url of the product you want to monitor on amazom, then with use of BeautifulSoup, scaprs the website for the price of the product.
It does need a few headers for the amazon sequrity protocal, the headers can be found on http://myhttpheader.com/, the two headers that work for me are
"User-Agent" and "Accept-Language".
