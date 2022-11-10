To use this system you require the following things:
anaconda(the system has only been tested in windows, so if possible use windows please): https://www.anaconda.com/
python: https://www.python.org/

open anaconda powershell prompt
the path should be "Your path/mysite/mysite/
This can be done using the "cd" command
in this case use "cd mysite/mysite" use the tab button to help you
create the environment using the command "conda create --name myenv"
when prompted type "y" to confirm
start environment with command "conda activate myenv"
install django with command "conda install -c anaconda django"
when prompted type "y" to confirm
To run the system you need to start the local server first
to do this type the command "python manage.py runserver 8080"
Go to the address given (it is normally "http://127.0.0.1:8080/"
for any issues with this refer to: https://docs.djangoproject.com/en/4.0/intro/tutorial01/
To stop the server click "Ctl-C"

When you now want to ever run the server and use the system you would need to 
make sure your in this folder Your path/mysite/mysite/
run "conda activate myenv"
type the command "python manage.py runserver 8080"
Go to the address given (it is normally "http://127.0.0.1:8080/"
