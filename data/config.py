from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')  # Забираем значение типа str
ADMINS = env.list('ADMINS')  # Список администраторов бота
IP = env.str('ip')  # Тоже str, но для ip адреса хоста
URL_APPLES = env.str('URL_APPLES')
URL_PEAR = env.str('URL_PEAR')
