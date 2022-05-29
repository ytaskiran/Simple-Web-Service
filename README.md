# Simple-Web-Service
A small web service for Devpaths program homework

This was very simple implementation for a web service. In order to scale this service, first I need to create and manage a database (for example a database that is optimized for distributed computing like Dynamo) to store the values with POST requests. For now, this app just stores a hashmap and all data vanishes when the program exits.

I deployed the application on Heroku because of its simplicity. Also it is free to use. If this service becomes more complicated and gets more traffic, then I would need to deploy on another cloud web service platform to reach richer resources. 

In order to make this easy to maintain and make the deployment process more sustainable, I'd build a development pipeline and form rules that differs production level code and debug level code.
