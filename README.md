# Test_Bakcend_task

Задание:
- Напишите скрипт, асинхронно, в 3 одновременных задачи, скачивающий содержимое HEAD репозитория https://gitea.radium.group/radium/project-configuration во временную папку.
- После выполнения всех асинхронных задач скрипт должен посчитать sha256 хэши от каждого файла.
- Код должен проходить без замечаний проверку линтером wemake-python-styleguide. Конфигурация nitpick - https://gitea.radium.group/radium/project-configuration
- Обязательно 100% покрытие тестами

Для решения задачи, скачивающий содержимое HEAD репозитория, я использовал библиотеку GitPython

Сделал 2 решение:
1) main.py решил через multiprocessing
<img width="810" alt="image" src="https://user-images.githubusercontent.com/70702619/228180569-d7704194-d290-44ea-94b8-4175d904a583.png">


2) another_main.py через asyncio
<img width="1148" alt="image" src="https://user-images.githubusercontent.com/70702619/228180477-c7e60d38-6d17-4f47-b2b6-9c31e2ca8995.png">



Тесты дорабатываются 

<img width="388" alt="image" src="https://user-images.githubusercontent.com/70702619/228180775-6ba91ab6-e1d4-4cf2-8bfb-1c79f26db9ee.png">

