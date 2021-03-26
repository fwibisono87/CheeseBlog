# CheeseBlog
Hello and welcome to the *CheeseBlog!*

This project is intended as an entry for the Faculty of Computer Science's RISTEK Backend Web Development application process, by yours truly, [fwibisono87](http://www.franciswibisono.com)!

The admission task are to make a blog website with the following specifications:
1. User registration and login
2. User can perform CRUD operations on blogs
3. User can view all blogs
4. User can create comments on blogs

As of the current deployed state, requirements 1 through 4 have been shipped.

This project utilizes the Django Framework

*this project is deployed at [cheeseblog.franciswibisono.com](http://cheeseblog.franciswibisono.com)*<br>
*this project has a Git repository hosted at [https://github.com/fwibisono87/CheeseBlog](https://github.com/fwibisono87/CheeseBlog)*

##Installation Instructions
You can just use the deployed one, but you might be interested in hosting your own instance of CheeseBlog (for whatever reason, lol.) If so, follow the following (heheh) instructions!
1. Install `Python` on your system (preferabbly the latest `3.x` version) [here](https://www.python.org/downloads/)
2. Install `git` on your system [here](https://git-scm.com/)
3. Clone this repository (or, you know, just download the source code) into your system
4. Open the directory where you copied/cloned/downloaded this repository
5. Access your favourite terminal emulator (`powershell` for windows or `terminal` for linux)
6. Run the command `python3 --version` to check if your Python installation is properly configured
7. Attention Ubuntu/Debian users! You need to install the module `python3-venv` from the apt repository!
8. Run the command `Python -m venv cheeseblog` to configure a virtual environment for Django to run
9. For Windows, run the command `cheeseblog/Scripts/activate` to activate your virtual environment, For Linux/macOS, run `source cheeseblog/bin/activate` instead.
10. Next, to satisfy all Django requirements, change your directory to the project root folder then run `pip install -r requirements.txt`
11. This distribution *should* be ready to run out of the box, however, to make sure that everything is set, run the following commands:
12. `python manage.py collectstatic`
13. `python manage.py makemigrations`
14. `python manage.py migrate --run-syncdb`
15. Optionally, you might want to assign yourself as a superuser. If so, run `python manage.py createsuperuser` and follow the prompt.
16. Finally, to start the server, run the command `python manage.py runserver`
