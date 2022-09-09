Web App for analysts to enter their stock finding. Basic CRUD for the moment. Development for Openshift deployment.
Still in development, tests have to be done, styling have to be done. 

See basic Instruction down here :

We are deploying the app to Openshift
We use command line OP CLI for that:

The setting.py has a postgresql database set up for openshift or for normal django+postgresql project:
To run migrations:
python3 manage.py migrate
BUT migration have already been set in aap.py which is recognized by Openshift that will run all commands listed in that file.
I used that to launch the server as well with Gunicorn.

We use gunicorn to serve the app in the pod and have a script in app/py that will migrate the database and runserver



Deployment:
- Your postgresql database:
oc new-app postgresql POSTGRESQL_USER=<your_user_name> POSTGRESQL_DATABASE=<your_database_name> POSTGRESQL_PASSWORD=<your_password>

- Your github repo app (Openshift will recogniwe and read from app.py):
oc get pods -o wide # to get the ip address of your Openshift deployed postgresql IP address
oc new-app --strategy=source <openshift_compatible_os_image>~<your_github_repo_url>.git#<your_branch> DJANGO_SECRET_KEY="<set_a_long_secret_key_string>" DATABASE_SERVICE_NAME=<openshift_postgresql_service_name(like DNS)> DATABSE_NAME=<database_user> DATABASE_USER=<user> DATABASE_PASSWORD=<password>

- Create a route when your application is deployed. Deploy Postgresql before your application.

We successfully used: centos/python-38-centos7


Routes in the App:
/ # to get to the indexpage
/report # to get the Reports and be able to add your Financial findings about stocks around the world
/loginuser # to login
/logoutuser # to logout
/registeruser # to register
/updateinfo/<int:pk> # to update database entry
/delete/<int:pk> # to delete database entru
/update/<int:pk> # to update database entry

