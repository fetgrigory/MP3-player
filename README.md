# MP3-player
Данная программа представляет собой аудиоплеер, который позволяет воспроизводить различные форматы аудиофайлов. Она имеет простой и интуитивно понятный пользовательский интерфейс, который обеспечивает удобное управление воспроизведением музыки.<br />
Код оформлен в соответствии с требованиями flake8, что обеспечивает читаемость и качество кода.
![Снимок экрана 2024-11-12 131203](https://github.com/user-attachments/assets/07908e35-67c2-4524-824e-a0dba79538e7)<br />
# Основные функции программы:
1. Воспроизведение аудиофайлов: Вы можете выбрать аудиофайлы форматов ASF, FLAC, MP4, Monkey's Audio, Musepack, Ogg Opus, Ogg FLAC, Ogg Speex, Ogg Theora, Ogg Vorbis, True Audio, WavPack, OptimFROG и AIFF и воспроизводить их в программе. Она поддерживает как сжатые форматы с потерей качества, так и без потери. Для добавления аудиофайлов нужно нажать на кнопку "Добавить", если нужно удалить нажать на кнопку "Удалить"
2. Управление воспроизведением: Программа позволяет вам контролировать воспроизведение музыки. Вы можете использовать кнопки "Играть", "Пауза", "Стоп" и "Перемотка" для управления воспроизведением.
3. Регулировка громкости: В программе есть ползунок громкости, который позволяет вам настроить уровень звука во время воспроизведения музыки. Вы можете увеличить или уменьшить громкость в зависимости от своих предпочтений.
4. Беззвучный режим: Программа предоставляет возможность включить и выключить звук плеера. Если вам нужно временно отключить звук, вы можете нажать на кнопку "Беззвучный режим".
### Подготовка виртуального окружения и запуск программы

1. Создайте виртуальное окружение для изоляции зависимостей проекта. 
   Используйте команду:
   ```bash
   python -m venv venv
   ```

2. Активируйте виртуальное окружение:
   - На Windows:
     ```bash
     venv\Scripts\activate
     ```
   - На macOS и Linux:
     ```bash
     source venv/bin/activate
     ```
3. Запустите программа командой:
   ```bash
   python main.py
   ```
# Инструкция по использованию программы:<br />
Шаг 1: Запуск программы
1. Найдите и откройте файл MP3-player.exe. (При наличии ошибки «api ms win crt runtime l1 1 0 dll» необходимо установить компонент Visual C++: https://docs.microsoft.com/ru-RU/cpp/windows/latest-supported-vc-redist?view=msvc-170)
2. Появится окно программы с интерфейсом аудиоплеера. <br />
Шаг 2: Выбор аудиофайла для воспроизведения
1. Нажмите кнопку "Играть".
2. Откроется окно для выбора файла.
3. Перейдите к месту, где хранятся ваши аудиофайлы, и выберите файл формата MP3, WAV, OGG, AAC, FLAC или AIFF, который вы хотите воспроизвести.
4. Нажмите кнопку "Открыть" в окне выбора файла. <br />
Шаг 3: Управление воспроизведением музыки
После выбора файла, музыка начнет воспроизводиться автоматически.
Используйте кнопку "Пауза", чтобы приостановить воспроизведение музыки.
Нажмите кнопку "Воспроизвести", чтобы возобновить воспроизведение музыки.
Чтобы остановить воспроизведение музыки, нажмите кнопку "Стоп".
Если вы хотите вернуться к началу музыки, нажмите кнопку "Перемотка".<br />
Шаг 4: Регулировка громкости
Чаще всего в аудиоплеерах есть ползунок громкости, который позволяет регулировать уровень звука.
Переместите ползунок вправо, чтобы увеличить громкость.
Переместите ползунок влево, чтобы уменьшить громкость.<br />
Шаг 5: Беззвучный режим
В аудиоплеере также есть кнопка "Беззвучный". Нажмите на нее, чтобы отключить звук плеера.
Нажмите кнопку снова, чтобы вернуть звук обратно.<br />
Шаг 6: Завершение работы программы
Чтобы остановить воспроизведение музыки и завершить работу программы, нажмите кнопку "Стоп" или закройте окно программы.
## Применяемые библиотеки:<br />
pygame 2.1.2 <br />
mutagen 1.45.1 <br />
ttkthemes 3.2.2 <br />
