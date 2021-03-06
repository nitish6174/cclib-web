# Configuration for docker environment

import os

# Used to set : app.config['SEND_FILE_MAX_AGE_DEFAULT']
static_file_max_age = 3600 * 24 * 7

# Computational chemistry log file directory
data_folder = "/data/"

# MongoDB variables
mongo_host = os.environ['DB_PORT_27017_TCP_ADDR']
mongo_port = "27017"
mongo_name = "openchemistry-web"
mongo_user = ""
mongo_pass = ""
