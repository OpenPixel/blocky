default: test


test_django:
	cd tests/blocky_django && python manage.py test

test_flask:
	cd tests && python blocky_flask.py

test: test_django test_flask
