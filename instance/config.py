# application confiiguration

import os 
dbpass="ZAQxswCDE321."
dbuser="GEp_Admin"
dbname = "asset1"
db_port = 5432
dbhost = "noleak-asset-integrity-server.postgres.database.azure.com"

SECRET_KEY = 'secret_key_must_be_safe'

DATABASE_URI = f'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
