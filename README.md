<!-- shields -->
![GitHub contributors](https://img.shields.io/github/contributors/atbeuth/beuth-ws1920-project)
![Host](https://img.shields.io/badge/Host-pythonanywhere-blue)
![Using](https://img.shields.io/badge/Using-Python%20--%20Django-yellowgreen)

<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img style="background: black; padding: 10px; border-radius: 20px;" src="https://photohubteam.pythonanywhere.com/static/icons/logo_photohub.png" alt="Logo" width="100" height="100">

  <h3 align="center">PhotoHub - Website</h3>

  <p align="center">
    Our semester project for the module "Projekt" at the Beuth University in Berlin
    <br />
    <a href="https://photohubteam.pythonanywhere.com/"><strong>Explore PhotoHub »</strong></a>
    <br /><br />

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## About The Project

<a href="https://ibb.co/4jDyKZ5"><img src="https://i.ibb.co/bryhQg8/PhotoHub.png" alt="PhotoHub" border="0"></a>

---
> We love pictures. We like the idea of making pictures usable for everyone and sharing art. However, we also want to give everyone the opportunity to distribute their pictures with a license of their choice. *Similar to software on GitHub*.
---

**For our project we decided on a photo platform and would like to make the following possible:**

* Easily upload and download images 📡

* Easily use individual licenses or use our PhotoHub license, which offers free use with the protection of the author 📃

* Build a library of searchable images 🏞🌌🌉

---

> We wanted to create something that we can continue to use after the end of the project. Therefore some features of the website may change in the future.

---

### Built With

* [Bootstrap](https://getbootstrap.com)
* [Django](https://www.djangoproject.com)
* [Python](https://www.python.org)

<!-- GETTING STARTED -->
## Getting Started
>If you would like to contribute to PhotoHub or like to help us testing, you can find information here on how to get a local version up and running.

### Prerequisites
* Python 3.7: [https://www.python.org/downloads/](https://www.python.org/downloads/) or `brew install python`
* git: https://git-scm.com

**We also recommend:**
* VS Codeium: [https://vscodium.com/](https://vscodium.com/) Editor
* SQLite Browser: [https://sqlitebrowser.org/dl/](https://sqlitebrowser.org/dl/) to look at the database entries

### Installation
1. Clone the repo:
```sh
git clone git@github.com:atbeuth/beuth-ws1920-project.git
```

2. We use [line-awesome](https://icons8.com/line-awesome)
    * Download the zip from [https://icons8.com/line-awesome/howto](https://icons8.com/line-awesome/howto)
    * Put the content in a folder 
    `/photo_webs/static/fonts`

3. Create virtual environment
*   Install virtualenv 
    ```sh
    pip install virtualenv
    ```
*   Start virtualenv
    ```sh
    virtualenv venv
    ```
*   Activate virtualenv
    ```sh
    source venv/bin/activate
    ```
*   Install dependencies
    * cd into the project directory
    ```sh
    pip install -r requirements.txt
    ```

4. Secret Key
    * cd into /photo_webs/photo_webs
    * create a file ***secret_settings.py***
    * get secret key from [https://miniwebtool.com/django-secret-key-generator/](https://miniwebtool.com/django-secret-key-generator/)
    * open ***secret_settings.py*** and add 
    `SECRET_KEY = '<your key>'`

5. Migrate and run server
    * cd into the first photo_webs/
    * PhotoHub comes with migrations
    ```sh
    python manage.py migrate
    ```
    * run server
     ```sh
    python manage.py runserver
    ```
<!-- CONTACT -->
## Contact
Project Link: [https://github.com/atbeuth/beuth-ws1920-project](https://github.com/atbeuth/beuth-ws1920-project)

Imprint: [https://photohubteam.pythonanywhere.com/imprint](https://photohubteam.pythonanywhere.com/imprint/)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Pythonanywhere](https://www.pythonanywhere.com)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Line Awesome](https://icons8.com/line-awesome)
* [shields.io](https://shields.io/category/other)
