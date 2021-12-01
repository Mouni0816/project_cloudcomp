# project_cloudcomp
Prediction of house prices deplyed in cloud using ANN

Link = https://nicolasmounish-su5zcw76kq-ew.a.run.app

In this readme, we will discuss the creation of a prediction model and deployment of it in cloud using google cloud and docker. — House prediction with ANN.

Initially we created a model ANN that is going to be predicting the prices ofhouses based on three parameters, for this task we used a ANN model. 
For the data we scraped multiple real estate websites (seloger, century21...). the data consists of four columns (price of the houses, number of rooms, the level of the building and the surface area). We deemed these three variables as relevant to predict the house prices in our model.
We created a two page flask application of our model where we enter the parameters in one page and get the result on the second page. the model is saved in .h5 and is added to the project to evit the training of model each time it is launched to predict. 
In main.py we have the flask application and also a translator that is taking the input converting it into our desired format to put into our model.
We then created a docker file and a requirement.txt based on our environment. 

After this we connected our sdk shell to our google cloud account. Then we use the class material to deploy it online.

Cost = 11.50 dollar per month



