from utils import exportar_grafo, extraer_contenido_archivo, medir_cpu_ram
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from typing import TypedDict
import time
import logging

logging.basicConfig(
    filename="logs/ejecuciones.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

# Silenciamos librerías externas para evitar el ruido en el log
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


def ask_for_rubric() -> str:
    # TODO
    option = input("Rubrica 1 o 2: ")
    if option == "1":
        return extraer_contenido_archivo("./test/rubrica_nivel_1.txt")
    elif option == "2":
        return extraer_contenido_archivo("./test/rubrica_nivel_2.txt")


def ask_for_code() -> str:
    # TODO
    option = input("Codigo 1: ")
    if option == "1":
        return extraer_contenido_archivo("./test/python_code_test.py")


def define_graph():
    llm = ChatOpenAI(model="gpt-5-mini", temperature=0)

    # Definimos State
    class State(TypedDict):
        rubric: str
        code: str
        response: str

    # Definimos los nodos
    def retrieve_data(state: State) -> State:
        state["rubric"] = ask_for_rubric()
        state["code"] = ask_for_code()
        return state

    def evaluate_code(state: State) -> State:
        prompt = f"""Evalua este codigo en funcion de la rubrica, contesta solo con los criterios que cumple y los que no, indicando los fragmentos relevantes en cada caso pero sin enseñar la correccion:
Rubric:
{state["rubric"]}

Code:
{state["code"]}
"""
        response = llm.invoke(prompt)
        state["response"] = response.content
        return state

    def show_feedback(state: State) -> State:
        print(state["response"])
        return state

    # Creamos el graph y añadimos los nodos
    graph = StateGraph(State)
    graph.add_node("retrieve_data", retrieve_data)
    graph.add_node("evaluate_code", evaluate_code)
    graph.add_node("show_feedback", show_feedback)

    # Creamos las conexiones entre nodos
    graph.set_entry_point("retrieve_data")
    graph.add_edge("retrieve_data", "evaluate_code")
    graph.add_edge("evaluate_code", "show_feedback")
    graph.add_edge("show_feedback", END)

    return graph.compile()


def main():
    executor = define_graph()
    initial_state = {"rubric": "", "code": "", "response": ""}

    # Guardamos el tiempo que tarda en realizarse las ejecuciones
    inicio = time.perf_counter()
    end_state = executor.invoke(initial_state)
    fin = time.perf_counter()

    logging.info(
        f"Tiempo: {fin - inicio:.4f}s | "
        f"Lineas de codigo: {end_state["code"].count("\n")}"
    )

    exportar_grafo(executor, "exported_graph")


if __name__ == "__main__":
    main()
