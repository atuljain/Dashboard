# **64 Bit Consultants** #

This Project is for internal management for the **64 Bit Consultants** and completely built in house. Technologies used in the project are **Python2.7**, **Django1.8** and **Bootstrap**.

**Steps to Setup project locally:**

1. Ask Administrator to give you SSH keys, You can provide your public SSH key to the admin to add it in the account and give you access.

2. Clone the project repository using SSH access and command will be 
```
#!shell

git clone git@bitbucket.org:pankul/dashboard.git
```

3. Now create a virtual environment for the DayPlanner.

4. Activate the virtual Environment and make the project repository as your current directory.

5. Install all other dependencies by running
```
#!shell

pip install -r requirements.txt
```

6. Ask admin or team mates for a database dump.

7. Create a local settings file using the local_settings_sample and you should be able to run server using 
```
#!shell

python manage.py migrate

python manage.py runserver
```

If you are still facing any problem, Please contact at mittal.pankul@gmail.com
