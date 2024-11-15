import requests
from tqdm import tqdm
import urllib.parse


class FileDownloader:
   
   def __init__(self):
      pass

   def download(self, url, new_file_name = None):
    # Выполнение HTTP-запроса
    # Открываем соединение с сервером
    response = requests.get(url, stream=True)
    content_disposition = response.headers.get('content-disposition')
  # Извлечение части с именем файла
    prefix = "filename*=UTF-8''"
    start = content_disposition.find(prefix) + len(prefix)
    encoded_filename = content_disposition[start:]

    # Декодирование URL-кодирования
    original_filename_decoded = urllib.parse.unquote(encoded_filename)


    if (new_file_name):
        filename = new_file_name + '.' + original_filename_decoded.split('.')[-1]
    else:
        filename = original_filename_decoded




    total_size = int(response.headers.get('content-length', 0))  # Общий размер файла
    block_size = 1024  # Размер блока данных, который будет читаться за раз (1 KB)

    # Создаем индикатор прогресса
    tqdm_bar = tqdm(total=total_size, unit='B', unit_scale=True)

    with open(filename, "wb") as file:
        for data in response.iter_content(block_size):
            tqdm_bar.update(len(data))  # Обновляем индикатор прогресса
            file.write(data)  # Записываем данные в файл

    tqdm_bar.close()
    
    # Извлечение имени файла из заголовка 'Content-Disposition'

  
    return filename, original_filename_decoded

gi