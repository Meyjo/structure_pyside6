import os

# Lista de carpetas y archivos a crear (estructura basada en tu workspace)
structure = [
    'main.py',
    'README.md',
    'requirements.txt',
    'src/controllers/__init__.py',
    'src/controllers/config.py',
    'src/models/__init__.py',
    'src/resources/icons/',
    'src/resources/images/',
    'src/ui/__init__.py',
    'src/ui/py/',
    'src/ui/qt/',
    'src/utils/__init__.py',
    'src/views/__init__.py',
    'src/widgets/__init__.py',
    'tests/',
    '.gitignore'
]

def create_structure(base_path):
    module_folders = [
        'src/controllers',
        'src/models',
        'src/ui',
        'src/utils',
        'src/views',
        'src/widgets',
        'tests'
    ]
    created_dirs = set()
    for item in structure:
        path = os.path.join(base_path, item)
        if item.endswith('/'):
            os.makedirs(path, exist_ok=True)
            created_dirs.add(path)
        else:
            dir_name = os.path.dirname(path)
            if dir_name and not os.path.exists(dir_name):
                os.makedirs(dir_name, exist_ok=True)
                created_dirs.add(dir_name)
            if not os.path.exists(path):
                with open(path, 'w', encoding='utf-8'):
                    pass
    # Crear __init__.py en carpetas de módulos
    for folder in module_folders:
        abs_folder = os.path.join(base_path, folder)
        if os.path.exists(abs_folder):
            for root, dirs, files in os.walk(abs_folder):
                # Excluir cualquier carpeta dentro de resources
                if 'resources' in root.split(os.sep):
                    continue
                init_path = os.path.join(root, '__init__.py')
                if not os.path.exists(init_path):
                    with open(init_path, 'w', encoding='utf-8'):
                        pass

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Uso: python generate_structure.py <ruta_destino>')
        sys.exit(1)
    dest = sys.argv[1]
    create_structure(dest)
    print(f'Estructura creada en: {dest}')
