# Digital_Assistance_Bot_for_Pharmacy_using_Rasa_Framework
This is the project where we have build a chatbot for the pharmacy to get the details of the medicines when the symptoms of the customer is given. This chatbot we have made using the Rasa Framework

The goal of this project is to create a digitalized chatbot for the pharmacist so that without having much medical knowledge he/she can give the medicines to customer based on the symptoms they have. 

## The Architecture for our project is shown below:

![Project Architecture](https://user-images.githubusercontent.com/86455215/144393884-0b3dbb0f-2d33-45f3-b1ac-e171a66c85e9.png)

## Data Collection
The commplete data collection for the bot is done by using the web scraping concept. We have taken the [1MG website](https://www.1mg.com/drugs-listaz) for our data collection where we have collected all the information of the medicines using request, Beautiful Soup, Scrapy libraries for scrapping the data of 1mg Website.  

## Data Preparation for rasa chatbot
* After collecting the dataset by using webscrapping, we have prepared the data rasa framework by separating the data into three parts i.e. all the medicines and their I'd at one place, all the symptoms and their I'd at once place and We have linked the medicines with their particular symptoms in the other data set. A acreen shot of all the three data sets is shown below


![image](https://user-images.githubusercontent.com/86455215/144399183-8f004026-0dfe-4c38-87b7-9b5d9f02f9b2.png) ![image](https://user-images.githubusercontent.com/86455215/144399205-b2035fd8-72d1-4d58-a865-4aa5603ed4a5.png) ![image](https://user-images.githubusercontent.com/86455215/144399235-b4def0b9-d8d2-41ec-bf7a-828f216b2fe2.png)

* The main part of rasa framework is the data prepartion in that we have to generate the intents which is there in the data preparation folder in this repository.
In the data preparation folder there will a code for preparring the data and the output of the code will generate the intents for our bot and the screenshot of the same is shown below.

![image](https://user-images.githubusercontent.com/86455215/144400006-43906469-3e93-4b5a-b311-668777bb378a.png)

* Once the intents are generated we have to place the same in the nlu.md file which will be there in the data folder by giving some intent name to all the intents after that we have give that intent name in other files like domain.yml and stories.yml

* After data is prepared we have give the action to the bot in action.py file so that bot has to take the answers from the excell data which we have used.


## Model Building
* After preparing the data for the bot we have to train our complete model by giving the command rasa train in the command prompt
* After the model is trained with RASA NLU nad RASA CORE we can check the working of the bot by giving the command rasa shell so that we can talk with our bot in the command prompt only or else we can even talk with our bot in the web using the command rasa x.


## Tech used in the project
* Python 3.6
* Rasa 2.0
* Rasa X 
* request
* beautiful soup

## Once the complete bot is ready we can integrate the same with our website using the config file.
