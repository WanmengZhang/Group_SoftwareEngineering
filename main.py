import logging
import json
from classifier import classify_question
from evaluation import evaluate_scenario_question, evaluate_technical_question, evaluate_stress_question
import llm

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_reference_answer(question, user_answer):
    try:
        system_prompt = "你是一个面试者，请对面试问题做出回答，并根据以下答案进行润色和完善：\n"
        user_prompt = f"问题: {question}\n用户答案: {user_answer}"
        response = llm.answer(system_prompt, user_prompt)

        if isinstance(response, dict):
            return response.get('answer', 'No answer found.')
        else:
            return response.strip()
    except Exception as e:
        logger.error(f"Error generating reference answer: {e}")
        return ""

def evaluate_question(question):
    if not isinstance(question, dict):
        logger.error("Invalid question format. Expected a dictionary.")
        return "Invalid question format."

    question_text = question.get("question", "")
    answer = question.get("answer", "")

    if not question_text or not answer:
        logger.error("Question or answer is missing.")
        return "Question or answer is missing."

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
    # Read questions and answers from output.json
    with open('output.json', 'r', encoding='utf-8') as f:
        interview_data = json.loads(f.read())

    if not isinstance(interview_data, list):
        logger.error("Invalid interview data format. Expected a list of dictionaries.")
        return

    with open('results.txt', 'w', encoding='utf-8') as output_file:
        for question in interview_data:
            if not isinstance(question, dict):
                logger.error("Invalid question format in interview data. Expected a dictionary.")
                continue

            question_type = classify_question(question.get("question", ""))
            reference_answer = generate_reference_answer(question.get("question", ""), question.get("answer", ""))
            evaluation = evaluate_question(question)

            output_file.write(f"问题: {question.get('question', '')}\n")
            output_file.write(f"该问题属于{question_type}类型的问题\n")
            output_file.write(f"答案: {question.get('answer', '')}\n")
            output_file.write(f"参考答案: {reference_answer}\n")
            if isinstance(evaluation, dict):
                for key, value in evaluation.items():
                    output_file.write(f"{key}: {value}\n")
            else:
                output_file.write(f"评价: {evaluation}\n")
            output_file.write("\n")


if __name__ == "__main__":
    main()
