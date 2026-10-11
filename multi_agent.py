
from ollama import chat

MODEL = "qwen3.5:4b"


def run_agent(agent_name, system_prompt, user_message):
    print(f"\nStarting: {agent_name}")

    response = chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        think=False
    )

    print("Ollama role:", response.message.role)
    print("Agent:", agent_name)

    return response.message.content


question = input("You: ")

# Agent 1
answer = run_agent(
    "Python Teacher",
    "You are a Python teacher. Answer clearly with an example.",
    question
)

print("\nAGENT 1 ANSWER:\n", answer)

# Agent 2
reviewed_answer = run_agent(
    "Python Code Reviewer",
    "You are a Python code reviewer. Check the answer "
    "for mistakes and improve its clarity.",
    f"Question: {question}\nAnswer to review: {answer}"
)

print("\nAGENT 2 REVIEW:\n", reviewed_answer)
