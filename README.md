Swirl-CRM is a solo dev project for my learning and demonstration of my skills with Django.

	This follows the a tutorial on the YouTube channel JustDjango, and is marked in the 'credits.txt' file, in the root directory.

	Anyone is welcome to use this if they so desire;  however,  Swirl is not comparable to contemporary CRM software - if you are looking for a professional and free CRM, I believe HubSpot CRM is free, open source, and popular.

	If despite the above, you use this software, and desire any changes or features, let me know.  Be aware however, I am only one human!

	Thanks,

	T

To use this project locally, you will need to create a '.env' file within 'Swirl-CRM/Swirl-CRM/',  to appear as such:
	
	'Swirl-CRM/Swirl-CRM/.env'

You will then need to create a django secret key.  From the command line, ensuring django is installed within your active  environment, copy, paste and execute the following:

	python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'	

	A secret key will be generated and printed to the console.

	Copy the secret key.

Next open the .env file you have created at 'Swirl-CRM/Swirl-CRM/.env'

	you will need to type:

		DEBUG=True
		SECRET_KEY='[your secret key]'

	save and exit the '.env' file

Almost there!

Within the root directory of the project 'Swirl-CRM', set the environment variable READ_DOT_ENV_FILE=True

	Linux:
		
		export READ_DOT_ENV_FILE=True

	Powershell:
		
		$env:READ_DOT_ENV_FILE = 'True'

Finally
	
	python manage.py runserver

Access Swirl through a web browser at the appropriate address
