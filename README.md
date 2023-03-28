# Test_Bakcend_task

Задание:
- Напишите скрипт, асинхронно, в 3 одновременных задачи, скачивающий содержимое HEAD репозитория https://gitea.radium.group/radium/project-configuration во временную папку.
- После выполнения всех асинхронных задач скрипт должен посчитать sha256 хэши от каждого файла.
- Код должен проходить без замечаний проверку линтером wemake-python-styleguide. Конфигурация nitpick - https://gitea.radium.group/radium/project-configuration
- Обязательно 100% покрытие тестами

Для решения задачи, скачивающий содержимое HEAD репозитория, я использовал библиотеку GitPython

Сделал 2 решение:
1) main.py решил через multiprocessing
2) another_main.py через asyncio
