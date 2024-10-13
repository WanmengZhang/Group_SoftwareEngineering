import logging
from classifier import classify_question
from evaluation import evaluate_scenario_question, evaluate_technical_question, evaluate_stress_question
import llm

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_reference_answer(question):
    try:
        system_prompt = "你是一个面试者，请对面试问题做出回答。"
        response = llm.answer(system_prompt, question)

        if isinstance(response, dict):
            return response.get('answer', 'No answer found.')
        else:
            return response.strip()
    except Exception as e:
        logger.error(f"Error generating reference answer: {e}")
        return ""

def evaluate_question(question):
    question_text = question["question"]
    answer = question["answer"]

    # 使用AI模型对用户输入的答案进行评价
    system_prompt = f"对以下问题和答案进行评价:\n问题: {question_text}\n答案: {answer}"
    try:
        response = llm.answer(system_prompt, answer)
        evaluation = response.get('answer', 'No evaluation found.')
    except Exception as e:
        logger.error(f"Error evaluating answer: {e}")
        evaluation = "Error during evaluation"

    return evaluation

def main():
    interview_questions = [
        {
            "question": "二叉树的遍历方式有哪些？",
            "answer": "前序遍历。",
        },
    ]

    for question in interview_questions:
        question_type = classify_question(question["question"])
        reference_answer = generate_reference_answer(question["question"])
        evaluation = evaluate_question(question)
        print(f"问题: {question['question']}")
        print(f"该问题属于{question_type}类型的问题")
        print(f"答案: {question['answer']}")
        print(f"参考答案: {reference_answer}")
        if isinstance(evaluation, dict):
            for key, value in evaluation.items():
                print(f"{key}: {value}")
        else:
            print(f"评价: {evaluation}")
        print("\n")

if __name__ == "__main__":
    main()