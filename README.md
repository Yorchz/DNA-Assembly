# Proyecto de Ensamblaje de ADN con Grafos de De Bruijn

Este proyecto implementa un pipeline para ensamblar secuencias de ADN utilizando grafos de De Bruijn y encontrar un camino euleriano en el grafo generado a partir de k-mers. El código está modularizado en diferentes clases para cumplir con los principios de diseño SOLID, asegurando que cada clase tenga una única responsabilidad.

## Estructura del Proyecto

- **calculator/KmerProcessor**: Genera los k-mers a partir de las secuencias de ADN.
- **graph/BruijnGraphBuilder**: Construye el grafo de De Bruijn a partir de los k-mers generados.
- **graph/GraphVisualizer**: Visualiza el grafo de De Bruijn utilizando `networkx`.
- **calculator/EulerianPath**: Calcula el camino euleriano en el grafo de De Bruijn utilizando un método manual y otro basado en `networkx`.
- **calculator/DNAAssembler**: Ensambla la secuencia de ADN original a partir del camino euleriano encontrado.

## Descripción de las Clases y Funcionalidades

### 1. Generación de k-mers

La clase `KmerProcessor` recibe como entrada las secuencias de ADN y el tamaño `k` de los k-mers, generando una lista de substrings de longitud `k` que representan todos los k-mers posibles en las secuencias de entrada.

### 2. Construcción del Grafo de De Bruijn

La clase `BruijnGraphBuilder` toma los k-mers como entrada y crea un grafo dirigido en el que cada nodo representa un prefijo o sufijo de un k-mer, y cada arista representa una transición entre ellos. Este grafo es fundamental para identificar el camino euleriano necesario para ensamblar la secuencia de ADN original.

### 3. Visualización del Grafo de De Bruijn

La clase `GraphVisualizer` recibe el grafo de `networkx` y lo representa gráficamente, permitiendo visualizar las conexiones entre nodos (prefijos y sufijos de los k-mers).

### 4. Cálculo del Camino Euleriano

La clase `EulerianPath` implementa dos métodos para encontrar el camino euleriano:
- `find_path_manual`: Encuentra el camino euleriano de forma manual.
- `find_path_nx`: Utiliza la función `eulerian_path` de `networkx` para calcular el camino.

El camino euleriano representa la secuencia que conecta todos los nodos del grafo sin repetir aristas, crucial para la reconstrucción de la secuencia original.

### 5. Ensamblaje de la Secuencia de ADN

La clase `DNAAssembler` toma el camino euleriano (manual o de `networkx`) y ensambla la secuencia de ADN original. La salida final es la secuencia ensamblada en función del camino euleriano seguido.

## Requisitos

- Python 3.x
- `networkx` para la construcción y visualización del grafo de De Bruijn.
- `matplotlib` para la visualización gráfica (en caso de usar la animación).

## Instalación

Para instalar las dependencias del proyecto, ejecuta:

```bash
pip install networkx matplotlib
```

## Ejecución

1. Genera los k-mers de las secuencias de ADN.
2. Construye el grafo de De Bruijn a partir de los k-mers.
3. Visualiza el grafo de De Bruijn para observar las conexiones.
4. Calcula el camino euleriano utilizando el método manual o con networkx.
5. Ensambla la secuencia de ADN a partir del camino euleriano.

Este proyecto permite ensamblar secuencias de ADN de manera eficiente utilizando grafos de De Bruijn y caminos eulerianos, proporcionando una visualización clara y modularización adecuada para cada paso del proceso.
