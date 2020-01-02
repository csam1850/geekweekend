# setting up your workspace

## Installation requirements
### prerequisites
[git client](https://git-scm.com/download/win)  
[python 3.7.5 64-bit](https://www.python.org/ftp/python/3.7.5/python-3.7.5-amd64.exe)  
[vs code](https://code.visualstudio.com/download#)  
[docker for windows](https://docs.docker.com/docker-for-windows/install/)  

### vs code extensions
[python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)  
[code runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)  
[intelliCode](https://visualstudio.microsoft.com/de/services/intellicode/)  
[docker](https://code.visualstudio.com/docs/azure/docker)  


## set-up instructions
### how to use git
```bash
git echo "# geekweekend" >> README.md  
git init  
git add README.md  
git commit -m "first commit"   
git remote add origin https://github.com/csam1850/geekweekend.git  
git push -u origin master  
```

### setting up your python-workspace
Please note I deliberatly uploaded .vscode to github which contains hardcoded 
information from my personal workspace, which you need to adjust. The important
part is the PythonPath environment variable, which should point to your 
repository and not to your python.exe as one might expect from its name. 
If you encounter a Module-not-found error you probably have this issue.  
  

```shell
# this command creates a virtal environment  
python -m venv venv  
# activating the environment  
venv\Scripts\activate  
# installing the libraries with the specified version  
pip install -r requirements.txt
```

## starting the application
### starting local Flask-Server 

```shell
set FLASK_APP=app.py
flask run
```
  
### starting the docker container 
take care that the port is not blocked by the flask application

```shell
docker build -t classifier .
docker run -d -p 5000:5000 classifier
```

# Sources
## dataset
https://www.kaggle.com/moltean/fruits

## example models from kaggle
https://www.kaggle.com/mitch9090/fruit-dataset-image-classification-network  
https://www.kaggle.com/litzar/fruits-classification  
https://www.kaggle.com/aninditapani/cnn-from-scratch-with-98-accuracy  
https://www.kaggle.com/waltermaffy/fruit-classification-pca-svm-knn-decision-tree 

## example Flask-apps
https://github.com/OkanKY/keras-flask-webapp  
https://github.com/ibrahimokdadov/upload_file_python
  
# Tutorials
## creating docker images
https://code.visualstudio.com/docs/python/tutorial-create-containers  
https://code.visualstudio.com/docs/azure/docker  
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xix-deployment-on-docker-containers  

## deploying docker image
https://docs.microsoft.com/en-us/azure/app-service/containers/tutorial-custom-docker-image  
https://docs.microsoft.com/en-us/azure/python/tutorial-deploy-containers-01  

## using azure cognitive services
https://azure.microsoft.com/de-de/services/cognitive-services/custom-vision-service/  
https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/  
https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/getting-started-build-a-classifier  
https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/python-tutorial  
https://docs.microsoft.com/bs-latn-ba/azure/cognitive-services/custom-vision-service/export-your-model  
https://docs.microsoft.com/bs-latn-ba/azure/cognitive-services/custom-vision-service/export-model-python
