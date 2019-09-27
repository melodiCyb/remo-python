
from .sdk import SDK
from .domain.task import AnnotationTask


# see here: https://stackoverflow.com/questions/1944569/how-do-i-write-good-correct-package-init-py-files

# TBC read environemnt variable
config_file_path = 'C:/Users/Andrea.LaRosa/Desktop/'

config_file_name = 'remo.json'
config_file = config_file_path + config_file_name


sdk = SDK(server = config_file['server'],
          user_email = config_file['user_email'],
          user_password = config_file['user_password'])