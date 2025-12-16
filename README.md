# Unidad1-TareaRA1-MarioAntonClemente

## Descripción

Este proyecto es una simulación de un túnel de lavado de coches implementada en Python. La aplicación modela el proceso de lavado con diferentes fases y opciones personalizables como prelavado a mano, secado a mano y encerado. Incluye validaciones de reglas de negocio y un sistema de precios.

## Características

- **Simulación de fases**: El lavadero avanza por diferentes fases del proceso de lavado.
- **Opciones personalizables**: Prelavado a mano, secado a mano y encerado.
- **Validaciones de negocio**: Reglas como no permitir encerado sin secado a mano.
- **Sistema de precios**: Cálculo automático de costos basado en las opciones seleccionadas.
- **Pruebas unitarias**: Conjunto completo de pruebas para validar el funcionamiento.

## Requisitos

- Python 3.6 o superior

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/mantonc01/Unidad1-TareaRA1-MarioAntonClemente.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd Unidad1-TareaRA1-MarioAntonClemente
   ```

3. (Opcional) Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

## Uso

### Ejecutar la simulación

Para ejecutar una simulación básica, usa el archivo `main_app.py`:

```bash
python src/main_app.py
```

Este archivo contiene una función `ejecutarSimulacion` que demuestra el uso de la clase `Lavadero`.

### Usar la clase Lavadero

```python
from src.lavadero import Lavadero

# Crear una instancia del lavadero
lavadero = Lavadero()

# Iniciar un lavado con opciones
lavadero.hacerLavado(prelavado_a_mano=True, secado_a_mano=True, encerado=False)

# Avanzar por las fases
while lavadero.ocupado:
    lavadero.avanzarFase()
    print(f"Fase actual: {lavadero.fase}")

# Ver ingresos acumulados
print(f"Ingresos: {lavadero.ingresos} €")
```

## Estructura del proyecto

```
Unidad1-TareaRA1-MarioAntonClemente/
├── src/
│   ├── lavadero.py          # Clase principal Lavadero
│   ├── main_app.py          # Aplicación principal con ejemplo de uso
│   └── test_lavadero_unittest.py  # Pruebas unitarias
└── README.md                # Este archivo
```

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
python -m unittest src/test_lavadero_unittest.py
```

O usando pytest (si está instalado):

```bash
pytest src/
```

## Precios

- **Lavado básico**: 5.00 €
- **Prelavado a mano**: +1.50 €
- **Secado a mano**: +1.00 €
- **Encerado**: +1.20 € (requiere secado a mano)

## Reglas de negocio

1. El lavadero no puede iniciar un nuevo lavado si está ocupado.
2. No se puede solicitar encerado sin secado a mano.
3. Los ingresos se acumulan con cada lavado completado.

## Fases del lavado

1. Cobrando
2. Prelavado a mano (opcional)
3. Echando agua
4. Enjabonando
5. Pasando rodillos
6. Secado automático o a mano
7. Encerado (opcional)

## Reflexión sobre comparación de la infraestructura de seguridad de los lenguajes

### Introducción
En el desarrollo de software, la seguridad es un aspecto crítico que debe considerarse desde las primeras etapas del diseño. Los lenguajes de programación ofrecen diferentes niveles de infraestructura de seguridad integrada, que incluyen características como gestión de memoria, verificación de tipos, manejo de excepciones y herramientas para prevenir vulnerabilidades comunes. En este proyecto desarrollado en Python, reflexionaré sobre cómo se compara la infraestructura de seguridad de Python con otros lenguajes populares como Java, C++ y JavaScript.

### Python: Ventajas y desventajas en seguridad
Python es un lenguaje de tipado dinámico e interpretado, lo que ofrece flexibilidad y rapidez en el desarrollo, pero introduce ciertos riesgos de seguridad:

- **Gestión automática de memoria**: Python utiliza recolección de basura automática, lo que reduce errores comunes como fugas de memoria o accesos inválidos. Sin embargo, no previene problemas como race conditions en aplicaciones concurrentes.
- **Verificación de tipos en tiempo de ejecución**: A diferencia de lenguajes compilados con tipado estático, Python verifica tipos en ejecución, lo que puede llevar a errores de tipo no detectados hasta runtime.
- **Excepciones integradas**: El manejo de excepciones es robusto, pero requiere disciplina del programador para no exponer información sensible en traces.
- **Bibliotecas de seguridad**: Python cuenta con bibliotecas como `cryptography`, `PyJWT` y herramientas como `bandit` para análisis de seguridad, pero la responsabilidad recae en el desarrollador.

### Comparación con Java
Java, como lenguaje compilado con tipado estático, ofrece una infraestructura de seguridad más estricta:

- **JVM y verificación de bytecode**: La Máquina Virtual de Java verifica el bytecode antes de ejecución, previniendo muchos ataques de inyección.
- **Gestión de memoria**: Similar a Python, pero con mayor control sobre punteros y referencias, reduciendo vulnerabilidades como buffer overflows.
- **Ventaja sobre Python**: Java fuerza la declaración de tipos, detectando errores en compilación. Además, frameworks como Spring Security proporcionan capas de seguridad integradas.
- **Desventaja**: Java es más verboso, lo que puede llevar a más código boilerplate y potenciales errores humanos.

En comparación, Python es más propenso a errores de seguridad por su dinamismo, pero permite prototipos rápidos y es ideal para scripts y aplicaciones pequeñas como esta simulación.

### Comparación con C++
C++ es un lenguaje de bajo nivel con control total sobre la memoria, lo que lo hace poderoso pero peligroso:

- **Control manual de memoria**: Permite optimizaciones avanzadas, pero introduce riesgos como buffer overflows, use-after-free y dangling pointers, comunes en vulnerabilidades como Heartbleed.
- **Tipado estático estricto**: Detecta muchos errores en compilación, similar a Java.
- **Ventaja sobre Python**: Rendimiento superior y control granular, crucial para sistemas críticos.
- **Desventaja**: La complejidad aumenta el riesgo de bugs de seguridad. Herramientas como Valgrind ayudan, pero requieren expertise.

Python, al abstraer la gestión de memoria, reduce estos riesgos, haciendo que sea más seguro para desarrolladores no expertos, aunque menos eficiente.

### Comparación con JavaScript
JavaScript, especialmente en entornos web como Node.js, comparte similitudes con Python en dinamismo:

- **Tipado dinámico**: Similar a Python, lo que facilita desarrollo rápido pero introduce riesgos de inyección (XSS, CSRF).
- **Event-driven y asíncrono**: Frameworks como Express.js requieren atención a seguridad en APIs.
- **Ventaja sobre Python**: Mejor integración con web y ecosistema npm rico en herramientas de seguridad.
- **Desventaja**: JavaScript en navegador es vulnerable a ataques del lado cliente.

Python supera a JavaScript en consistencia de tipos y legibilidad, pero ambos requieren herramientas externas como linters y scanners para seguridad.

### Conclusión
La infraestructura de seguridad de Python es adecuada para aplicaciones como esta simulación, donde la simplicidad y rapidez son prioritarias sobre el rendimiento crítico. Sin embargo, para sistemas de alta seguridad, lenguajes como Java o C++ ofrecen mejores garantías integradas. La clave está en complementar cualquier lenguaje con prácticas de desarrollo seguro: revisiones de código, pruebas exhaustivas, uso de bibliotecas actualizadas y herramientas de análisis estático. En este proyecto, implementé validaciones de entrada y manejo de excepciones para mitigar riesgos comunes, demostrando que incluso en Python se puede lograr un código razonablemente seguro con buena práctica.

## Autor

Mario Anton Clemente

## Licencia

Este proyecto es parte de una tarea académica.

Mario Anton Clemente

## Licencia

Este proyecto es parte de una tarea académica.</content>
<parameter name="filePath">c:\Users\alumno\Desktop\Unidad1-TareaRA1-MarioAntonClemente\README.md