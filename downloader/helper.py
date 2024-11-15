import subprocess

def resolve_direct_yandex_url(url):
  # Выполняем команду с использованием переменной
  command = f"yadisk-direct {url}"
  command_output = subprocess.check_output(command, shell=True)

  # Декодируем байты в строку и удаляем лишние пробелы и символы новой строки
  return command_output.decode('utf-8').strip()

