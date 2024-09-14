# Django PollApp Documentation

# Introduction

The Django Poll App is a simple web application where users can create polls, vote on them, and view the results. This app serves as an example for learning Django's core concepts, including models, views, templates, and the Django admin interface.

This documentation covers the architecture, modules, key functions, and how the app works under the hood.

# Project Overview

The Django Poll app consists of two primary models:

Question: Represents a poll question with a publication date.

Choice: Represents an option in a poll, linked to a Question and tracking the number of votes.

# Key Features

1. Create polls with multiple choices.
2. Users can vote on polls.
3. View the results of a poll in real time.
4. Admins can manage polls using the Django admin interface.

# Architecture

The Django Poll app follows the **Model-View-Template (MVT)** architecture pattern:

. **Model**: Defines the data structure of the application (e.g., questions and choices).
. **View**: Handles the logic and processing of requests, fetching data from models, and rendering templates.
. **Template**: Controls how the data is presented to the user (HTML).

**How it works**

1. **Models** define the database structure (questions, choices, votes).
2. **Views** retrieve data from models and pass it to templates.
3. **Templates** render the data as HTML for the browser.
4. **Admin Interface** allows admins to manage questions and choices directly from a web interface.

# Core Interface

1.**`models.py`**

Defines the data structure for the application. Key models include:

**.** **Question:**

**.** `question_text` : The text of the poll question.

**.** `pub_date` : The date the poll was published.
![image](https://github.com/user-attachments/assets/0bcb5754-b52d-430f-bcf1-2776a65ae554)

**.** **Choice**

**.** `choice_text` : The text for a specific choice in a poll

**.** `votes` : The number of votes this choice has received.

**.** `question` : A foreign key linking this choice to a `Question`.
![image](https://github.com/user-attachments/assets/916e03ba-4890-497b-9b25-c8ec32bfc00f)

2.**`views.py`**

Handles the logic for displaying polls and results, as well as recording votes. Key views include:

**.** **Index view** : Displays a list of all available polls.
![image](https://github.com/user-attachments/assets/a666e4ea-54b1-450d-9df6-ef01f304e73f)

**.** **Detail View** : Displays the details of a specific poll, including it's polls
![image](https://github.com/user-attachments/assets/408652a1-863b-41f5-b2df-c3c45c843ba2)

**.** **Results View** : Displays the results of a specific poll
![image](https://github.com/user-attachments/assets/ddccb84e-dcca-4dd0-a79d-cb7206880d5f)

**.** **Vote view** : Handles the logic for voting on a poll choice.
![image](https://github.com/user-attachments/assets/7173345b-1de0-4f67-b5a4-26095f5364b1)

3. **`urls.py`**

This file maps URL patterns to views. Some key routes include:

**.** `/polls/` : Displays the index view with a list of polls.

**.** `/polls/<id>/` : Displays the details of a specific poll.

**.** `/polls/<id>/results/` : Show the results of a poll.

**.** `/polls/<id>/vote/`: Submits a vote for a poll choice.
![image](https://github.com/user-attachments/assets/568cb154-0998-4e5d-903a-8fdbcbf8dc37)

4.**`templates\`**

The templates folder contains HTML files that render the data passed by views:

**.** **index.html**: Lists all polls

**.** **detail.html**: Displays a specific poll and it's choices.

**.** **results.html**: Displays the result of a poll after voting.

Example of a template(**detail.html**):
![image](https://github.com/user-attachments/assets/c26fe2fc-5c9c-49fd-b814-f645d3e4cca1)

5.**`admin.py`**

The admin module allows for easy management of polls through the Django admin interface. The `Question` and `Choice` models are registered to make them accessible via the admin panel.
![image](https://github.com/user-attachments/assets/ac50220c-c7b2-4f0e-a188-90c32799b3dc)

# Admin Interface

The Django Poll app comes with an admin interface that allows superusers to:

**.** Add, modify, or delete polls (questions).

**.** Manage poll choices.

**.** View and manage votes.

 To access the admin interface, visit `/admin/` after setting up a superuser account.

 # Testing 

 The app includes basic unit tests in the tests.py file. These tests check the logic of the views, models, and other key components.

Run the tests using:
![image](https://github.com/user-attachments/assets/75f39ada-5028-47ee-b83c-a35ea0a37aac)

# Extending the App

You can easily extend the Poll app by:

**.** Adding new models or fields to existing ones.

**.** Creating new views or templates for custom functionality.

**.** Integrating the app with APIs for data retrieval or analytics.

























