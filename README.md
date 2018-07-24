# Slack Questions App

This is a Slack application which is used to periodically share questions on a specific slack channel. This project is still in development.
It uses [Serverless Framework](https://serverless.com/), for which Node10.3 is needed and Python3 for the codebase.

## Resources Used

This section lists the resources used for the entire project.
### API
This section lists the resources used for the API. At the moment, the API is **NOT** secure.

- AWS API Gateway
- AWS Lambda
- AWS S3

### Database
This section lists the resources used for the data layer.

- MongoDB
- AWS SSM

## Resource Setup
### MongoDB
For this project, I used MongoDB from [MongoAtlas](https://www.mongodb.com/cloud/atlas), however you can use your own MongoDB store with the key parameters we need are :

1. **Connection String**: This is URL for the MongoDB cluster. This is the connection string to the database on the MongoDB cluster. It may look something like this 
    > mongodb+srv://<CLUSTER_NAME>.mongodb.net/questionsdb?retryWrites=true
    
    where `questionsdb` is the name of the database.
2. **MongoDB User Credentials**: The username and password with `Read` and `Write` access to the above mentioned database.

Add the **connection string** and **user credentials** to the `ssmparameters.py` file.

#### MongoDB Atlas Instructions

1. Create an account and project on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. Create a cluster.
3. Once the cluster is created, head over to `Cluster > Security > MongoDB Users`. Create a user with `Read` and `Write` Permissions to the cluster.
Make a note of the `username` and `password`.
4. Head over to `Cluster > Security > IP Whitelist` and allow access from everywhere.
5. Connect to the MongoDB Cluster and create a database. I used a GUI tool called [Studio 3T](https://studio3t.com/) to monitor the cluster.

### Slack

The following is a guide to create a [Slack App](https://api.slack.com/) for a specific channel in your workspace.

1. Create a Slack App [here](https://api.slack.com/).
2. Add webhooks to you application by heading over to the `Incoming Webhooks` section.
3. Create a webhook for the channel on which your application will publish the questions and authorize it.
4. Take a note of the webhook URL which would look something like this:
`https://hooks.slack.com/services/Ofj49Ng/Kfm738sj/Ufb739sKkmfl9`. In this URL, `/Ofj49Ng/Kfm738sj/Ufb739sKkmfl9` is our **Webhook URL Substring** which we use in the application.
5. Enter that string into `ssmparameters.py`. 


## Deployment
Before installing, we need the following:

- A **Node** environment for `serverless`.
- A **Python3** environment for deploying the code and debugging.
- A **Docker** Daemon running for packaging the python packages into a custom docker image.
- AWS CLI with programmatic Access Keys configured.

To run the installation script run:

```console
foo@bar:~$ python deploy.py
```
 