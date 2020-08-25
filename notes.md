# Notes

Below is a list of commonly forgotten concepts that I needed to relearn in making this. Figured it's a good idea to write them down for a more painless process in the future.

## Setting up the database

- `models.py` sets up the tables
- `manage.py` is for maintaining the migrations

### Database Migrations

Initialize the database using the flask-migrate commands. After having the boilerplate code inside of `manage.py` type the following commands to begin version control on the db:

```bash
python manage.py db init    # only needed once for initial setup
python manage.py db migrate # analyze any changes to db since last upgrade
python manage.py db upgrade # lock in the changes from the generated alembic file
```

In subsequent updates to the db, only use `migrate` and `upgrade`. Pretty sure there is a `downgrade` command or something like it.

Also, it can be helpful to check the generated python upgrade file in the `/migrations/versions` directory and make any necessary adjustments.
