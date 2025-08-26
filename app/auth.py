from passlib.context import CryptContext

# Informando ao passlib qual o algoritmo de criptografia (hash) padrão (bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
  """
  A função verifica se a senha em texto puro corresponde ao hash (código JWT) salvo.
  """
  return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
  """
  A função serve para gerar o hash (a criptografia) de uma senha em texto puro.
  """
  return pwd_context.hash(password)