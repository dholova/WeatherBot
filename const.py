# api.openweathermap.org/data/2.5/weather?q=London&appid=1439efb68806299b2a4de0f959e90f9e
TOKEN = '6042873140:AAHwGDBJ6kpnXW9G9_G6SgFW_CUF5XmiDjs'

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = '334511336'

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data


WEATHER_TOKEN = '1439efb68806299b2a4de0f959e90f9e'

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric'
