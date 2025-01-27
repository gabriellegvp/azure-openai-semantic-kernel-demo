import os
import openai
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configura a chave de API do Azure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Função para gerar uma resposta do modelo GPT-3.5
def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

# Função principal
def main():
    print("Bem-vindo ao Chatbot de Integração Azure OpenAI e Semantic Kernel")
    print("Digite 'sair' para encerrar.")
    
    while True:
        user_input = input("Você: ")
        
        if user_input.lower() == "sair":
            print("Encerrando o chatbot.")
            break
        
        # Gerando resposta com base no input do usuário
        prompt = f"Responda de forma inteligente e concisa: {user_input}"
        response = generate_response(prompt)
        
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
