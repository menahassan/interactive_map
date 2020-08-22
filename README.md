# interactive_map
Welcome to our project!

Group members:
Elizabeth Sinyavin (esinyavin01@gmail.com or sinyavin@stanford.edu), 
Mena Hassan (menah9@gmail.com), 
Thong Do (thobado1999@gmail.com), 
Ruth Fekade (fekad22r@mtholyoke.edu).

With both interactive and non-interactive elements, we hope our project will be useful for the museum. We chose this project because we wanted to help reduce the information barrier between the government and the people. Today, tensions between the executive branch and the press are at an all-time high. Access to free reporting is a cornerstone of our democracy, which is why one of our primary focal points was developing a web scraping service to display the latest, most up-to-date reporting on the United States' relations with each country as well as on the world's most pressing global issues.

Highlights: 
- US diplomatic presence visualization: indicates where we do and don't have a diplomatic presence
- global issue data visualization
- web scraping to find news articles about:
  1) the US's relations with each country
  2) current events pertaining to relevant global issues
- automated non-interactive design (freestyle feature)
- language audio effects (plays the primary language of that country)
- time lapse on certain global issues

How our project can be developed further:
- improved news searching with textual analysis (e.g. regular expressions)
- improved "freestyle" feature
- adding images to popups (e.g. flags)
- adding more data-driven global issues to the drop-down menu
- adding another map visualizing which embassies are open at the present moment


Important files:
- map/views.py - renders html template 
- map/templates/map/index.html - html to be rendered
- map/news.py - uses the GoogleNews module to search the web for news

