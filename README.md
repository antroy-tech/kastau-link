## Kastau Link

**Kastau Link** is a Open Source project for make shorten urls. Made with Tailwind CSS and Flask.

![GitHub](https://img.shields.io/github/license/antheiz/kastau-link)
![GitHub Repo stars](https://img.shields.io/github/stars/antheiz/kastau-link?style=flat-square)


## Installation

1. Create virtual environment

	```
	python -m venv env
	```

2. Activate virtual environment

	Linux:
	```
	source env/bin/activate
	```

	Windows:
	```
	\env\Scripts\activate
	```

3. Install the requirements
	
	```
	pip install -r requirements.txt
	```

4. Run the project

	- **Copy the .env.example into .env**
	
		*Note: Default Database for this Project with SQLite*

		```
		SECRET_KEY=your_secret_key
		DATABASE_URL=sqlite:///shorturl.sqlite
		APP_SETTINGS=config.DevelopmentConfig
		FLASK_APP=app
		GOOGLE_CLIENT_ID=your_google_client_id
		GOOGLE_CLIENT_SECRET=your_google_secret_id
		CONF_URL=https://accounts.google.com/.well-known/openid-configuration
		```

	- **Database Migrations**

		- Initiate Database
			```
			flask db init
			``` 
		- Migrate Database
			```
			flask db migrate
			```
		- Apply Migration
			```
			flask db upgrade
			```

	- **Run the project**

		```
		flask run
		```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please follow [Contributing Guide](./CONTRIBUTING.md) before contributing.


## Can I deploy to my own domain?

The code is open for learning purpose, feel free to deploy to your own domain. 

## Author

KastauLink is created by <a href="https://antheiz.me">Theis Andatu</a>.


## License
Kastau Link is under [MIT License](./LICENSE).