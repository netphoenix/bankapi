from passlib.context import CryptContext

PWD_CONTEXT = CryptContext(schemes=['bcrypt'], deprecated='auto')

SECRET_KEY = 'dfgdfgbcvbngghlbsfngnghmfhmnfgbnghmhjmgndgmfmghjkd'
EXPIRE_JWT_TOKEN = 10
TOKEN_TYPE = 'Bearer'
ALGORTITHM = 'HS256'
