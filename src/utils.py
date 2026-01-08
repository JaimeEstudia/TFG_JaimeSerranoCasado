# Visualización: generamos un archivo para visualizar con mermeid
def exportar_grafo(executor, name: str):
    # Yo uso la extension de vscode "Markdown Preview Mermaid Support"
    with open("./mermaid_graphs/" + name + ".md", "w") as f:
        f.write("```mermaid\n")
        f.write(executor.get_graph().draw_mermaid())
        f.write("\n```")


if __name__ == "__main__":
    print("Estas ejecutando utils.py")
    pass
