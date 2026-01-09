import os


# Visualización: generamos un archivo para visualizar con mermeid
def exportar_grafo(executor, name: str):
    # Yo uso la extension de vscode "Markdown Preview Mermaid Support"
    with open("./mermaid_graphs/" + name + ".md", "w") as f:
        f.write("```mermaid\n")
        f.write(executor.get_graph().draw_mermaid())
        f.write("\n```")


# Archivos: extramenos el contenido de los archivos a str
def extraer_contenido_archivo(ruta) -> str:
    if not os.path.isfile(ruta):
        raise FileNotFoundError(f"No existe el archivo: {ruta}")

    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()


import psutil


def medir_cpu_ram():
    cpu_percent = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory()

    return {
        "cpu_percent": cpu_percent,
        "ram_total_gb": memoria.total / (1024**3),
        "ram_usada_gb": memoria.used / (1024**3),
        "ram_percent": memoria.percent,
    }


if __name__ == "__main__":
    print("Estas ejecutando utils.py")
    pass
