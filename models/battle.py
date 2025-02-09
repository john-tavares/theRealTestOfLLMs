class Battle:
    def __init__(self, starter, rival, judge, rounds=4):
        self.llm1 = starter
        self.llm2 = rival
        self.judge = judge
        self.rounds = rounds

    def run(self):
        messages = []
        for i in range(self.rounds):
            messages.append(f"\n=== Round {i+1} ===\n")
            print(f"\n=== Round {i+1} ===\n")
            response = self.llm1.generate_response()
            messages.append(f'{self.llm1.name} diz: \n\n{response}\n\n')
            print(f'{self.llm1.name} diz: \n\n{response}\n\n')
            self.llm2.add_context("user", response)
            self.text_to_speech(self.llm1.name, i+1, response)

            response = self.llm2.generate_response()
            messages.append(f'{self.llm2.name} diz: \n\n{response}\n\n')
            print(f'{self.llm2.name} diz: \n\n{response}\n\n')
            self.llm1.add_context("user", response)
            self.text_to_speech(self.llm2.name, i+1, response)
        
        self.judge.add_context(''.join(messages))
        judge_response = self.judge.generate_response()
        print('O juiz diz: \n\n', judge_response)
    
    def text_to_speech(self, model_name:str, round_number:int, response:str):
        speech_file_path = f"{model_name}_{round_number}.mp3"
        response = self.llm1.client.audio.speech.create(
            model="tts-1",
            voice="ash" if model_name == "chatgpt" else "onyx",
            input=response,
        )
        response.stream_to_file(speech_file_path)
