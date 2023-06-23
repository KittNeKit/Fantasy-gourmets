# Fantasy gourmets
A project, that offers a rich collection of recipes for dishes from fantasy worlds.

## Description

Do you think about a site, where you can take a recipe from some games and cook it in real life?

This is your solution. Fantasy Gourmets is a site where whoever has a chef account can create his own recipe from the game and share it with others.
## Check it out!
[Fantasy gourmets project deployed on Render](https://fantasy-gourmets.onrender.com)
## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Fantasy-gourmets
```

2. Change to the project's directory:
```bash
cd project-name
```
3. Сopy .env_sample file with your examples of env variables to your .env
file:
```
# Django Secret Key
DJANGO_SECRET_KEY=your_secret_key_here

# Django Debug Mode
DJANGO_DEBUG=1
```
Replace your_secret_key_here with your own secret key and choose the appropriate debug mode
4. Install the dependencies

```bash
pip install -r requirements.txt
```

5. Set up the database:

Run the migrations

```bash
python manage.py migrate
```

6. Use the following command to load prepared data from fixture to test:
```bash
python manage.py loaddata fixture_data.json
```

7. Start the development server
```bash
python manage.py runserver
```
8. Access the website locally at http://localhost:8000.
9. Log in by the test user:
```
username = user
password = user12345
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.


