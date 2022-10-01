## Intro
**Kastau Link** is a Open Source project for make shorten urls. Made with Tailwind CSS and Flask.

## Installation

- Create virtual environment

	```
	python -m venv env
	```

- Activate virtual environment

	Linux:
	```
	source env/bin/activate
	```

	Windows:
	```
	\env\Scripts\activate
	```

- Install the requirements
	
	```
	pip install -r requirements.txt
	```

- Run the project

	1. Copy the .env.example into .env

		```
		SECRET_KEY=your_secret_key
		DATABASE_URL=your_db_access_url
		APP_SETTINGS=config.DevelopmentConfig
		FLASK_APP=app
		GOOGLE_CLIENT_ID=your_google_client_id
		GOOGLE_CLIENT_SECRET=your_google_secret_id
		CONF_URL=https://accounts.google.com/.well-known/openid-configuration
		```

	2. Run the program

		```
		flask run
		```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please follow [Contributing Guide](./CONTRIBUTING.md) before contributing.


## Can I deploy to my own domain?

The code is open for learning purpose, feel free to deploy to your own domain. 



## License
Kastau Link is under [MIT License](./LICENSE).