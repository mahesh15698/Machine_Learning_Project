# Machine_Learning_Project
Software and account requirement.

1.Github Account

2.Heroku Account

3.VS code IDE

4.GIT cli

Creating conda environment
```
conda create -p mjenv python == 3.9 -y
```
```
conda activate mjenv/
```

OR
```
conda activate mjenv
```
```
pip install -r requirement.txt
```
To add files to git
```
git add .
```
OR
```
git add <file_name>
```
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```
To check all version maintained by git 
```
git log
```
To create version/commit all changes by git
```
git commit -m "message"
```
To send version and changes to git hub 

```
git push origin main
```
To check remote URL
```
git remote -v
```
To setup CI/Cd pipeline in heroku we need 3 information
1.Heroku_Email
2.Heroku_API_Key = 3a5bd501-e44d-4251-8b44-ca3062c733e3
3.Heroku_APP_Name

Build Docker Image
```
docker build -t <image_name>:<tag_name> .
```
Note: Image name for docker is must be lower case

To list docker image
```
docker images
```
To run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image id>
```
