# Interactive Map - Impact Hack 2020
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
- map/templates/map/index.html - main html to be rendered
- map/news.py - uses the GoogleNews module to search the web for news
- data folder - holds all data visualization map files

Images and Demos:
- Embassy Map with markers (red for embassies/consulates, blue for countries in which the US does not currently have a diplomatic presence):
![Embassy Map](https://github.com/menahassan/images/blob/master/embassy%20markers.PNG)
- A marker popup showing the embassy/consulate, name country, and buttons to display the news or play the primary language:
![Popup](https://github.com/menahassan/images/blob/master/marker%20popup.png)
- A menu to allow the user to explore a specific country, global issue, or loop through embassies randomly with freestyle mode
![Explore Menu](https://github.com/menahassan/images/blob/master/exploremenu.png)
- Display if a user were to choose a global issue (ex: air pollution would show only the top 10 most polluted countries)
![Air Pollution](https://github.com/menahassan/images/blob/master/airpoluutiontitle.PNG)
![Air Pollution](https://github.com/menahassan/images/blob/master/airPoluutionmap.png)
- Popup if a user clicks on a global issue country marker (shows global issue data and top global news issue article in that country)
![Air Pollution Marker](https://github.com/menahassan/images/blob/master/airpollutionmarker.png)
- Freestyle Mode (loops through markers randomly without user interaction)
![freestyle gif](https://github.com/menahassan/images/blob/master/freestyle_mode.gif)
- Displays top 2 news articles in a country when user clicks "Get latest news" on popup
![news](https://github.com/menahassan/images/blob/master/news.png)
- Data map shows the years each embassy opened (from 1925 to 2020)
![embassy_years](https://github.com/menahassan/images/blob/master/embassy_map.gif)
- Data map shows the population change for each country around the world (from 1980 to 2020)
![world Population](https://github.com/menahassan/images/blob/master/world_pop.gif)
- Data map visualizes human trafficking data in 2018 
![human trafficking](https://github.com/menahassan/images/blob/master/humanTraficking.png)
