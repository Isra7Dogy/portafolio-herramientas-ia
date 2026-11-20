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
    """Recibe una imagen (PIL.Image o numpy.ndarray) y devuelve un diccionario
    con las 3 etiquetas más probables y su porcentaje (0 a 100)."""
    if imagen is None:
        return {}

    resultados = clasificador(imagen, top_k=3)

    return {
        item["label"]: round(float(item["score"]) * 100, 2)
        for item in resultados
    }


demo = gr.Interface(
    fn=clasificar,
    inputs=gr.Image(type="pil", label="Sube o arrastra una imagen"),
    outputs=gr.Label(num_top_classes=3, label="Top 3 etiquetas (%)"),
    title="¿Qué hay en la foto?",
    description="Utiliza el modelo google/mobilenet_v2_1.0_224 para identificar las 3 etiquetas más probables de una imagen.",
)

if __name__ == "__main__":
    demo.launch() 