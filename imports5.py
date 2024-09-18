import os
import importlib.util
import tensorflow
# Путь к текущему файлу main.py
current_file_path = __file__

# Путь к директории, где находится main.py
current_dir_path = os.path.dirname(current_file_path)

# Путь к директории folder
myfolder_path = os.path.join(current_dir_path, 'folder', 'underFolder')

# Путь к файлу functions.py в директории folder
functions_path = os.path.join(myfolder_path, 'functions.py')

# Загрузка модуля functions.py из директории folder
spec = importlib.util.spec_from_file_location("folder_functions", functions_path)
folder_functions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(folder_functions)

"""functions_path = os.path.join(os.path.dirname(__file__), 'folder', 'underFolder', 'functions.py')
spec = importlib.util.spec_from_file_location("folder_functions", functions_path)
folder_functions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(folder_functions)"""

# Используем функции из модуля folder_functions
folder_functions.print_rectangle_area(10, 5)
