from transformers import pipeline

class Question_Answer():
    def __init__(self):
        self.model_path = 'G:/Django/all_model/anil/roberta-base-squad2/'
        self.load_model = pipeline('question-answering', model= self.model_path)

    def process(self, context, question):
        output = self.load_model(question=question, context=context)
        return output