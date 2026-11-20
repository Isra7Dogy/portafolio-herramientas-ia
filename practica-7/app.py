from pathlib import Path
import time
import gradio as gr
import torch
from transformers import pipeline

# Usar GPU si está disponible, de lo contrario CPU
device = 0 if torch.cuda.is_available() else -1

# Cargar el pipeline de clasificación de imágenes con MobileNetV2
clasificador = pipeline(
    task="image-classification",
    model="google/mobilenet_v2_1.0_224",
    device=device,
)


def clasificar(imagen):
    """Recibe una imagen y devuelve:
    1) diccionario con las 3 etiquetas más probables y su porcentaje (0 a 100),
    2) tiempo de inferencia en segundos con dos decimales.
    """
    if imagen is None:
        return {}, "0.00 s"

    if torch.cuda.is_available():
        torch.cuda.synchronize()
    inicio = time.perf_counter()

    resultados = clasificador(imagen, top_k=3)

    if torch.cuda.is_available():
        torch.cuda.synchronize()
    fin = time.perf_counter()

    tiempo_seg = f"{fin - inicio:.2f} s"
    etiquetas = {
        item["label"]: round(float(item["score"]) * 100, 2)
        for item in resultados
    }

    return etiquetas, tiempo_seg


# Buscar imágenes dentro de la carpeta ejemplos/
carpeta_ejemplos = Path("ejemplos")
extensiones_validas = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}

ejemplos = []
if carpeta_ejemplos.exists() and carpeta_ejemplos.is_dir():
    ejemplos = [
        [str(ruta)]
        for ruta in sorted(carpeta_ejemplos.iterdir())
        if ruta.is_file() and ruta.suffix.lower() in extensiones_validas
    ]

demo = gr.Interface(
    fn=clasificar,
    inputs=gr.Image(type="pil", label="Sube o arrastra una imagen"),
    outputs=[
        gr.Label(num_top_classes=3, label="Top 3 etiquetas (%)"),
        gr.Textbox(label="Tiempo del modelo"),
    ],
    title="¿Qué hay en la foto?",
    description="Utiliza el modelo google/mobilenet_v2_1.0_224 para identificar las 3 etiquetas más probables de una imagen.",
    examples=ejemplos or None,
)

if __name__ == "__main__":
    demo.launch() 