# Hello!
This repository contains two algorythms, one is to request and save the current cards
of your jira repository in the especified project in the data.JSON once a day; 
The second one retrieves those infos and plots a burndown graphic.

## Installing all the necessary packages
Clone or download this repository and execute the code bellow in your CMD to install all
the necessary packages:
```pip install -r requirements.txt```

## How to run
### First of all!!!
Open the ```credentials.json``` file and set your infos to access your jira repository;
The OAuth token can be created in your Jira profile security settings.

### Files:
* main.py - requests the data in the jira database and saves it into the ```data.json``` file. The keys for the data object will be the request day and the values will be another object with each status name and cards quantities
* retrieve_graphic.py - will format and plot the burndown graphic with all the infos saved in the ```credentials.json```

If you have any issue to run the code, send an email to igor64br@gmail.com
