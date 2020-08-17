#!
# use source venv/bin/setup.sh to execute

export DATABASE_NAME="quick_poll"
export DB_USERNAME="postgres"
export DB_PASSWORD="postgres"
export DB_HOST="localhost:5432"
export DATABASE_URL="postgresql://${DB_USERNAME}:${DB_PASSWORD}@${DB_HOST}/${DATABASE_NAME}"