# 🐝 Hive Fundraiser - Backend 🐝

Welcome to the Hive Fundraiser backend repository. This project was created for a software testing lesson. This is where all the magic happens to support our fundraising platform.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

```Shell
git clone https://github.com/mhas1381/Django-Advanced-Blog.git
```


### 📋 Running project with docker ⛴

```Shell
docker compose up
```



### 🔧 Running project with virtual env

```Shell
pip install virtualenv
```
Windows setup:
```Shell
#creating the enviroment
python -m venv venv

#activating the enviroment
venv\Scripts\activate

#deactivating enviroment
deactivate
```
Linux and Mac setup:
```Shell
#creating the enviroment
python -m venv venv

#activating the enviroment
source venv/bin/activate

#deactivating enviroment
deactivate
```

then installing the requirements:

```Shell
pip install -r requirements.txt
```
### Running the Project
in order to run the project you need to use either ways below

default and development settings
```Shell
python manage.py runserver 
```

## 🏃 Running the tests

```Shell
pytest .
```

## 🛠️ Built With

* ![django](https://img.icons8.com/material-outlined/24/django.png) - Django framework
* ![nginx](https://img.icons8.com/color/48/nginx.png) - Nginx
* ![posgressql](https://img.icons8.com/color/48/postgreesql.png) - Posgres sql for database

## 📚 Curriculum

- Setting up project with Docker (dockerfile/docker-compose)
- Setup Django Model for a Blog and AbstractBaseUser
- Implement Class Based Views
- Django RestFramework and Serializers (FBV)
- ClassBasedViews in RestFramework (views,generic,viewset)
- Api Documentation with swagger and redoc
- Authentication API (Token/JWT)
- Reformat and Lint (flake8,black)
- Django TestCase and PyTest
- Django CI with github actions
- Populate Database with Faker and Django Commands
- Cores Headers
- Load Testing with Locust
- Get ready for deploy (gunicorn/nginx)
- Use postgres sql as a database
- Use google smtp server

## 📐 Model Schema

![Model Schema](./model-schema.png)

## 🤝 Contributing

Please read [CONTRIBUTING.md](link) for details on our code of conduct, and the process for submitting pull requests to us.

## 🎉 Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## 👥 Authors

* **Your Name** - *Initial work* - [Mohammad Husein Asnavandi]([https://github.com/YourName](https://github.com/mhas1381))


## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## 🙏 Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
