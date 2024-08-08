class Ai:
    def __init__(self):
        from os import system
        try:
            import ollama
        except ModuleNotFoundError:
            system('pip install ollama')
            import ollama

        self.class_ollama = ollama
        system("ollama pull llama3.1")
        ollama.pull("llama3.1")

    def ask(self, prompt: str) -> str:
        answer = self.class_ollama.chat(
            model="llama3.1",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        full_answer = ""
        for chunk in answer:
            full_answer += chunk["message"]["content"]

        return full_answer
