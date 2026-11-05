# No soy ni me parezco, Si soy yo

**Este proyecto ayuda a encontrar un perro perdido a traves de la comparación de su foto y el perro que se vio en la calle**

**Proyecto integrador · Herramientas de IA**

**Grupo:** A1 · **Equipo:** Mascotas

## 👥 Integrantes

|Nombre completo|Matrícula|
|---|---|
|Pablo Israel Avalos Moreno|
|Hector Ulises Serrano Ramos|
|Jessica Abigail|
|Maria Isabella Rangel Gutierréz|

## 1. Caso de uso

Poder identificar un perro que se ha perdido a traves de una comparacion entre la del perro perdido y uno que lo estan buscando.

- **Entrada:** El usuario propociona una fotografia en formato digital de la cara o cuerpo completo del animal que se quiere conocer el parentesco con uno perdido
- **Salida:** El sistema genera un vector de caracteristicas y devuelve el porcentaje de parentesco entre las imagenes

## 2. Modelo abierto elegido

|Dato|Respuesta|
|---|---|
|Identificador|[AvitoTech/DINO-v2-small-for-animal-identification](https://www.google.com/url?q=https%3A%2F%2Fhuggingface.co%2FAvitoTech%2FSigLIP2-Base-for-animal-identification)|
|Tarea (pipeline tag)|`image-feature-extraction (Extracción de Embeddings para Re identificación)`|
|Número de parámetros| 22,000,000|
|Licencia|Apache 2.0 |
|Limitación o sesgo declarado| Disminución en la precisión de identificación cuando las fotografías presentan iluminación deficiente, ángulos muy inclinados o cuando el rostro/cuerpo de la mascota se encuentra parcialmente ocluido.|

## 3. Viabilidad de hardware

Memoria mínima=N×2 bytes≈ ? GB

$$
\text{Memoria mínima} = N \times 4\ \text{bytes} \approx \ ?\ \text{GB}
$$

$$
\text{Memoria mínima} = 22,100,000 \times 4\ \text{bytes} \approx 88,400,000\ \text{bytes}
$$


- **VRAM disponible en Colab:** 14  GB (GPU-T4)
- **Dónde se ejecuta:** Colab on GPU
- **Por qué:** Se ejecutará en Google Colab con GPU. El modelo requiere únicamente ~88.4 MB, lo que representa menos del 5% de la VRAM asignada por Colab. Esto garantiza una inferencia rápida y local sin exceder los recursos del entorno gratuito ni depender de cuotas de una API externa.

## 4. Riesgo ético

- **Riesgo:** Posible error en la comparación de imágenes, y a futuro, pueden existir riesgos mayores debido al uso de datos personales. 
- **Mitigación:** Para nuestro riesgo actual (comparación falsa) podemos definir de manera más precisa los parámetros de las comparaciones. 

## 5. Evidencia
![Model card](Modelhug.png)


## Como funciona
```mermaid
flowchart TD
    A([Inicio]) --> B[/Usuario ingresa 2 imágenes/]
    B --> |Fotografías digitales| C[Modelo DINOv2]
    C --> D[Extracción de características]
    D --> |Vectores de rasgos| E[Comparación de embeddings]
    E --> F[Cálculo de similitud coseno]
    F --> G{Resultado de similitud}
    G --> |Coincidencia válida| H([Posible coincidencia del perro/gato])
	G --> |Sin coincidencias| I[Solicitar nueva fotografia]
	I --> |Reintento| B
```

