from utils import exportar_grafo
from langgraph.graph import StateGraph, END
from typing import TypedDict


def main():
    exportar_grafo(ejemplo23(), "prueba23")


# Ejemplo 2.3
def ejemplo23():
    # Definimos el state
    class EchoState(TypedDict):
        input: str
        output: str

    # Definimos un nodo que lee el state y lo actualiza
    def echo_node(state: EchoState) -> EchoState:
        user_input = state["input"]
        response = f"You said: {user_input}"
        state["output"] = response
        return state

    # Construimos y conectamos el graph
    graph = StateGraph(EchoState)
    graph.add_node("echo", echo_node)
    graph.set_entry_point("echo")
    graph.add_edge("echo", END)

    executor = graph.compile()

    initial_state = {"input": "LangGraph is clean."}
    result = executor.invoke(initial_state)
    print(result["output"])
    return executor


if __name__ == "__main__":
    main()
