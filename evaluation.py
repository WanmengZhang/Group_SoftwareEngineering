# evaluation.py

def evaluate_scenario_question(answer):
    criteria = {
        "问题理解": "候选人是否理解问题的核心。",
        "创新性": "候选人是否提出了创新的解决方案。",
        "逻辑性": "候选人的回答是否有逻辑性。",
        "适应性": "候选人是否能够适应不同的情景。"
    }

def evaluate_technical_question(answer):
    criteria = {
        "准确性": "候选人的回答是否准确无误。",
        "深度": "候选人是否展现出对问题的深入理解。",
        "广度": "候选人是否能够展示对相关领域的广泛知识。",
        "解决问题的能力": "候选人是否能够提出有效的解决方案。"
    }

def evaluate_stress_question(answer):
    criteria = {
        "冷静度": "候选人是否能够保持冷静，不被问题激怒或困扰。",
        "应变能力": "候选人是否能够迅速思考并给出合理的回答。",
        "自信度": "候选人在回答问题时是否表现出自信。"
    }