## PWC-SMS SPAM Detection Assignment
## ML-Model-Flask-Deployment
This is an assignment/coding test from PWC to test the resource on how the given Machine Learn Model (SMS SPAM Dection) is deployed on production using Flask API, Containers (Docker) and Kubernetes

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has four major parts :
1. model.py - This contains code fot our Machine Learning model to predict a given SMS is a SPAM OR HAM, the dataset used for this model is https://www.kaggle.com/uciml/sms-spam-collection-dataset#spam.csv
2. app.py - This contains Flask APIs that receives a text through GUI or API calls, computes the predicted value (SPAM/HAM) based on our model and display the message on the page/return the same
3. templates - This folder contains the HTML template to allow user to enter SMS text and displays the predicted message SPAM/HAM.

### Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000 (Example: http://127.0.0.1:5000/)

You should be able to view the homepage as below :
(HomePage.png in the given files)

Enter any SMS message to check whether it is a SPAM OR HAM

If everything goes well, you should  be able to see the predcited message with SPAM OR HAM like below:
(HAM.png and SPAM.png in the given files)

############
KUBERNETES
############
## Deploy SMS SPAM Detection assignment on Google Kubernetes Engine
##Steps followed as part of this assignment:
- Build a Docker image and upload it on Google Container Registry (GCR).
- Create clusters and deploy machine learning model with Flask app as a web service.
- See a web app in action that uses a trained machine learning model (SMS SPAM detection) to predict on the new data points in real-time.















