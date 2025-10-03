# PySide6 Project Structure Generator

Un generador automático de estructura de proyectos para aplicaciones PySide6, diseñado para crear una base sólida y organizada para tus proyectos de GUI en Python.

## 🚀 Características

- **Estructura MVC organizada**: Separación clara entre modelos, vistas y controladores
- **Configuración lista para usar**: Archivos de configuración y dependencias preconfigurados
- **Carpetas de recursos**: Directorios organizados para iconos e imágenes
- **Componentes modulares**: Estructura que facilita la escalabilidad del proyecto
- **Archivos `__init__.py` automáticos**: Generación automática en todos los módulos de Python

## 📁 Estructura del Proyecto Generado

```
proyecto/
├── main.py                     # Punto de entrada de la aplicación
├── README.md                   # Documentación del proyecto
├── requirements.txt            # Dependencias del proyecto
├── .gitignore                 # Archivos y carpetas a ignorar en Git
├── src/
│   ├── controllers/           # Lógica de control y configuración
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models/                # Modelos de datos
│   │   └── __init__.py
│   ├── resources/             # Recursos estáticos
│   │   ├── icons/            # Iconos de la aplicación
│   │   └── images/           # Imágenes y recursos gráficos
│   ├── ui/                    # Archivos de interfaz de usuario
│   │   ├── __init__.py
│   │   ├── py/               # Archivos .py generados desde Qt Designer
│   │   └── qt/               # Archivos .ui de Qt Designer
│   ├── utils/                 # Utilidades y funciones auxiliares
│   │   └── __init__.py
│   ├── views/                 # Vistas de la aplicación
│   │   ├── __init__.py
│   │   └── cashview.py
│   └── widgets/               # Widgets personalizados
│       └── __init__.py
└── tests/                     # Pruebas unitarias e integración
```

## 🛠️ Instalación y Uso

### Prerrequisitos

- Python 3.7 o superior
- Sistema operativo: Windows, macOS o Linux

### Uso Rápido

1. **Clona o descarga este repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/create_structure_pyside6.git
   cd create_structure_pyside6
   ```

2. **Ejecuta el generador**:
   ```bash
   python generate_structure.py <ruta_destino>
   ```

   **Ejemplo**:
   ```bash
   python generate_structure.py mi_proyecto_pyside6
   ```

3. **¡Listo!** Tu estructura de proyecto PySide6 está creada y lista para usar.

### Ejemplo de Uso Detallado

```bash
# Crear un nuevo proyecto en el directorio actual
python generate_structure.py ./mi_app_gui

# Crear un proyecto en una ruta específica
python generate_structure.py "C:\Proyectos\mi_nueva_app"

# Crear un proyecto en tu directorio de trabajo
python generate_structure.py ~/Desarrollo/mi_proyecto
```

## 🎯 Casos de Uso

Este generador es perfecto para:

- **Proyectos PySide6/PyQt6**: Aplicaciones de escritorio con interfaz gráfica
- **Desarrollo ágil**: Inicio rápido de proyectos sin configuración manual
- **Equipos de desarrollo**: Estructura consistente entre proyectos
- **Prototipado rápido**: Base sólida para pruebas de concepto
- **Aplicaciones empresariales**: Estructura escalable y mantenible

## 🔧 Personalización

Puedes modificar el archivo `generate_structure.py` para adaptar la estructura a tus necesidades:

```python
# Modifica la lista 'structure' para agregar/quitar carpetas y archivos
structure = [
    'main.py',
    'README.md',
    # Agrega tus propios archivos y carpetas aquí
    'src/database/__init__.py',    # Ejemplo: módulo de base de datos
    'src/api/__init__.py',         # Ejemplo: módulo de API
]
```

## 📋 Contenido Incluido

### Archivos Base
- `main.py`: Archivo principal de la aplicación
- `README.md`: Documentación del proyecto
- `requirements.txt`: Lista de dependencias
- `.gitignore`: Configuración para Git

### Módulos Organizados
- **Controllers**: Lógica de negocio y configuración
- **Models**: Estructuras de datos y modelos
- **Views**: Interfaces y vistas de usuario  
- **Widgets**: Componentes personalizados
- **Utils**: Utilidades y funciones auxiliares
- **Resources**: Recursos estáticos (iconos, imágenes)

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el generador:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Agrega nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🆘 Soporte

Si encuentras algún problema o tienes preguntas:

- **Issues**: [Crear un issue](https://github.com/tu-usuario/create_structure_pyside6/issues)
- **Documentación**: Revisa este README
- **Ejemplos**: Consulta los casos de uso arriba

---

⭐ **¡Si este proyecto te fue útil, no olvides darle una estrella!** ⭐