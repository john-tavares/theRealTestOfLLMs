from dotenv import load_dotenv
from models.llm import RapperLLM
from models.battle import Battle
from models.judge import Judge
import os

load_dotenv()

chatgpt = RapperLLM("chatgpt", api_key=os.getenv("OPENAI_API_KEY"))
deepseek = RapperLLM("deepseek", api_key=os.getenv("OPENROUTER_API_KEY"))
judge = Judge(model="meta-llama/llama-3.3-70b-instruct", api_key=os.getenv("OPENROUTER_API_KEY"))

battle = Battle(starter=chatgpt, rival=deepseek, judge=judge, rounds=4)
battle.run()