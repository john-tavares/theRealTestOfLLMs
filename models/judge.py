import openai

class Judge:
    def __init__(self, api_key:str, model:str):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://openrouter.ai/api/v1"
        self.prompt = """Atue como um avaliador de uma batalha de rap e dê uma nota de 0 a 10 para cada participante.
            Sua avaliação deve ser baseada na criatividade e qualidade das rimas geradas.
            As respostas devem ser ricas em detalhes e explicar o motivo da nota.
            >>> Seja objetivo nas respostas e só d6e uma nota final com justificativa. <<<
            No final, apresente a nota final de cada participante e o vencedor.
            >>> Utilize palavras simples para qualquer pessoa entender. <<<
        """
        self.context = [{"role": "system", "content": self.prompt}]
        self.client = openai.OpenAI(base_url=self.base_url, api_key=self.api_key)

    def add_context(self, response):
        self.context.append({"role": "user", "content": f"{response}"})
    
    def generate_response(self):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.context,
        )
        self.add_context(response.choices[0].message.content)
        return response.choices[0].message.content