import llm
from data import data

def classify_question(question):
    # Create the system prompt
    system_prompt = f"根据以下数据：{data}，请判断\"{question}\"应属于什么类型的面试题，只输出类型，无需分析"
    # Use the AI model to classify the question
    response = llm.answer(system_prompt, question)
    return response.get('answer', 'Unknown')