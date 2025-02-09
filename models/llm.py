import openai

class RapperLLM:
    def __init__(self, name, api_key):
        self.name = name
        self.api_key = api_key
        if self.name == "chatgpt":
            self.model = "gpt-4o"
            self.base_url = "https://api.openai.com/v1"
            self.rival = "Deepseek"
        else:
            self.model = "deepseek/deepseek-chat"
            self.base_url = "https://openrouter.ai/api/v1"
            self.rival = "ChatGPT"

        self.client = openai.OpenAI(base_url=self.base_url, api_key=self.api_key)
        self.prompt = f"""Você é o modelo {self.name} e esta em uma batalha de rap insana.
            Este é o seu Rival: {self.rival}, não tenha pena dele.
            Seus insultos devem se concentrar na história da empresa do seu rival (OpenAI ou Deepseek).
            >>> Lembre-se de sempre rimar e ser criativo. <<<
            Usem insultos e não tenha pena do seu adversário, mas não usem palavrões. 
            Sempre referenciando a resposta anterior para aumentar a tensão.
            >>> Utilize palavras simples para qualquer pessoa entender. <<<
            Responda somente com uma rima de 4 linhas.
        """
        self.context = [{"role": "system", "content": self.prompt}]

    def add_context(self, role:str, response):
        self.context.append({"role": role, "content": f"{response}"})
    
    def generate_response(self):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.context,
        )
        self.add_context("assistant", response.choices[0].message.content)
        return response.choices[0].message.content