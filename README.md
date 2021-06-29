# Company Employee Management tool 

Hosted on Heroku - http://djangocomp.herokuapp.com/ -> Please wait for sometime , it may take a while to load the site

## This is an Django based Company-Employee tool which helps for management of various Companies and their employees data. 
- You have the ability to add new company , delete old company and edit the details of each company
- Users can access each company model and add new employees , delete employees and edit the employee details
- At last users can also download the PDF of each company employee list and save it


# Here are Screenshots from the 

## Company Home Page
![1](https://github.com/AKXAT/Company_Admin_Management/blob/main/ScreenShots/1.png)

## Employee of each company
![2](https://github.com/AKXAT/Company_Admin_Management/blob/main/ScreenShots/2.png)

## Add New Employee 
![3](https://github.com/AKXAT/Company_Admin_Management/blob/main/ScreenShots/3.png)

## Download the PDF
![4](https://github.com/AKXAT/Company_Admin_Management/blob/main/ScreenShots/4.png)

## Setps to setup an initail Djanog Project


##### Setting up the enviornment 
1. Create a new virtual enviornment using the command -> conda create --name DjangoEnv django
2. Activate that enviornment using the command -> conda activate DjangoEnv
3. In case you want to see how many virtual Env are there in the system then you may use the command -> conda info --envs


##### Setting up the project and the application
1. use the following commands to start project and make your first application -> django-admin startproject mysite. Then cd to the project and start app -->django-admin startapp company
2. include the urls.py and forms.py into the application that you just created 
3. add the application into the settings.py folder of the project(mysite)
4. Make the migrations -> python .\manage.py migrate and then register the application -> python .\manage.py makemigrations company
5. Just to confirm everything works you can try running the server -> python .\manage.py runserver

##### Now first lets setup the Models first
1. Now setup the Models where we defined the two models - company and the employee.


##### Now setup the forms.py
1. We need to add a forms.py file inside the application folder 
2. Import the models 
3. create classes and meta sub class also give the model name and the fileds you want


