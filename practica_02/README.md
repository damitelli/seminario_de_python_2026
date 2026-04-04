markdown

# Seminario de Python 2026 - Practica 02

# 🚀 Guía de Instalación: Jupyter Lab (Entorno Virtual)

Esta guía explica cómo configurar un entorno virtual aislado e instalar **Jupyter Lab** en los principales sistemas operativos para poder ejecutar el programa.

## 📋 Requisito previo
Antes de comenzar, se necesita **Python** instalado (versión 3.7 o superior).  

Verificar con:

Linux/macOS:
```bash
python3 --version
```

Windows
```bash
python --version
```

---

## Paso 1: Crear el Entorno Virtual


En este paso se crea la carpeta del entorno (llamada 'env').

Abrir una terminal en la carpeta del proyecto y ejecutar:


Linux/macOS:
```bash
python3 -m venv .venv
```

Windows:
```bash
py -m venv .venv
```

---

## Paso 2: Activar el Entorno


Linux/macOS:
```bash
source .venv/bin/activate
```

Windows:
```bash
.venv\Scripts\activate
```

---

## Paso 3: Instalar Jupyter Lab


Con el entorno activo, ejecutar los siguientes comandos:

### 1. Asegurarse de tener pip actualizado

Linux/macOS:
```bash
python -m pip install --upgrade pip
```

Windows:
```bash
py -m pip install --upgrade pip
py -m pip --version
```

### 2. Instalar Jupyter Lab

```bash
pip install jupyterlab
```

---

## Paso 4: Iniciar Jupyter Lab

```bash
jupyter lab
```

En caso de que no abra automaticamente se puede acceder a través de:
```bash
localhost:8888/lab
```