## A simple Django notes app
You can install this app simply by running following commands on command
line:

```sh
pip install -r requirements.txt
./manage.py makemigrations # 
./manage.py migrate        # make database structures
```

And to run, just type these:
```sh
./manage.py runserver
```

### REST API
The application have several APIs to communicate with back-end:

| Route         | Method | Action         |
| :------------ |:------:| :------------: |
| auth/register | POST   | Register User  |
| auth/login    | POST   | Login User     |
| auth/logout   | GET    | LogOut User    |
| notes         | POST   | Create a Note  |
| notes/<ID>    | GET    | Get a Note     |
| notes/<ID>    | DELETE | Delete a Note  |
| notes/<ID>    | PATCH  | Update a Note  |


## LICENSE
This Application is published under MIT License.
