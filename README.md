# Linked-Open-Data-web-application
Individual Project of Yuning Li

This is a web application that presents a linked data cloud [1] from the European Data Portal and allows users to perform related query functions.
To be able to run the web application, the user needs to install the Python environment and the very important Flask library. Once everything is configured and ready, the user runs app.py to start the application.
## Each specific file of the web application is described below.

app.py: an instance of Flask and is used to receive requests from the web server，the main program that starts the whole web application.
Static:
echarts.min.js: a JavaScript plugin that uses various charts to display statistical analysis results.
jquery-2.2.1.min.js: a compressed version of the jQuery library.
bootstrap.min.js: a compressed version of bootstrap's collection of all JavaScript commands.
bootstrap.css: complete generic stylesheet
The above four files are from the official website.[2,3,4]
style.css: custom style sheet
img.png: background image of the web application [5]
HTML:
index.html: the home page, showing the cross-domain data
cities.html: visualization for linked data in cities
international.html: visualization for linked data in international issues
transport.html: visualization for linked data in transport
health.html: visualization for linked data in health
energy.html: visualization for linked data in energy
education.html: visualization for linked data in education
introduction: page with introduction to the project
search.html: page for searching datasets by category or publisher
result.html: page for showing the search results to querying by category
result_publisher.html: page for showing the search results to querying by publisher
data.json: data that has been processed through Neo4j and Python

The folder "data" contains data from six categories. It should be noted that the data collection process collected all RDF data for the six categories, but due to the sheer volume, the dataset shown here is part of the dataset used for visualization. The visualization of more linked data is mentioned in the "Future work" section of the report.

References:
[1] The official portal for European data. [Online]. Available: https://data.europa.eu/en. [Accessed: Jul. 2, 2022].
[2] Apache ECharts. [Online]. Available: https://echarts.apache.org/en/index.html. [Accessed: Jul. 18, 2022].
[3] jQuery. [Online]. Available: https://jquery.com/. [Accessed: Jul. 15, 2022].
[4] Bootstrap. [Online]. Available: https://getbootstrap.com/. [Accessed: Jul. 15, 2022].
