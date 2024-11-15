from setuptools import setup, find_packages

setup(
    name="downloader",  # Название вашего модуля
    version="0.1.1",  # Версия
    packages=find_packages(),  # Автоматически находит все пакеты
    install_requires=[  # Зависимости, если они есть
        # "numpy",
        # "requests"
    ],
    url="https://github.com/ai-collab-incubator/downloader",  # URL вашего репозитория
    author="pauchai",
    author_email="paul.khimyack@gmail.com",
    description="file downloader ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
