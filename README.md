# 📘 Algorithms-Python

Este repositorio contiene los apuntes y soluciones en Python desarrolladas a lo largo de la asignatura de **Algoritmos para juegos**, estructurado por temas. Cada carpeta incluye implementaciones y problemas trabajados en clase.


## Índice por Temas

### Tema 0 – Introducción a Python
- Fundamentos del lenguaje Python: sintaxis, estructuras, funciones, entrada/salida.
- Ideal como pseudocódigo ejecutable en resolución de algoritmos.

---

### Tema 1 – Fundamentos de Algoritmia
- Definición y propiedades de los algoritmos.
- Análisis de eficiencia con notaciones O, Ω, Θ.
- Técnicas clásicas de diseño: divide y vencerás, voraces, backtracking, dinámica, etc.
- Introducción a clases de complejidad P, NP, y NP-completo.

---

### Tema 2 – Algoritmos sobre Grafos
- Búsqueda en profundidad **(DFS)** y Búsqueda en anchura **(BFS)**.
- Ordenación topológica, componentes fuertemente conexas.
- Detección de ciclos, cierre transitivo, bipartición.
- Puntos de articulación, caminos de longitud fija.

---

### Tema 3 – Algoritmos Voraces
- Construcción de soluciones óptimas locales paso a paso.
- Problemas tratados:
  - **Cambio de monedas**
  - **Mochila**
  - **Minimización de tiempos de espera**
  - **Planificación con fechas límite**

---

### Tema 4 – Voraces sobre Grafos
- **Árboles de expansión mínima**:
  - Kruskal
  - Prim
- **Caminos mínimos**:
  - Dijkstra
- **Heurísticas aproximadas**:
  - Coloreado de grafos
  - Problema del viajante

---

### Tema 5 – Divide y Vencerás
- Técnica basada en dividir el problema, resolver subcasos y combinar soluciones.
- Ejemplos implementados:
  - **Búsqueda binaria** – O(log n)
  - **Ordenación por mezcla (Mergesort)** – O(n log n)
  - **Ordenación rápida (Quicksort)** – promedio O(n log n), peor O(n²)
  - **Multiplicación de enteros grandes**
  - **Multiplicación de matrices** – O(n^2.81)

---

### Tema 6 – Backtracking (Vuelta Atrás)
Técnica basada en recorrer de forma **profunda** un árbol implícito de soluciones, descartando ramas no prometedoras (poda). Ideal para:

#### Problemas tratados:
- **Mochila 0-1 con n tipos** – Selección de objetos sin repetición que maximiza valor sin exceder capacidad.
- **Problema de las N reinas** – Colocar N reinas sin que se ataquen (filas, columnas, diagonales).
- **Laberinto** – Buscar un camino desde entrada hasta salida en una matriz con obstáculos.
- **Coloreado de grafos** – Asignar colores a nodos sin que dos adyacentes compartan el mismo.
- **Ciclo hamiltoniano** – Encontrar un ciclo que recorra cada vértice exactamente una vez.

---
