import os
import pandas as pd 
from google import genai

GEMINI_API_KEY="KEY"

df = pd.read_csv('dados.csv')

client = genai.Client(api_key=GEMINI_API_KEY)


def gerar_mensagem_marketing(nome: str) -> str:
    """Gera uma mensagem de marketing personalizada sobre investimentos ou benefícios do cartão."""
    prompt = (
        f"Crie uma mensagem curta (máximo 140 caracteres) e amigável de marketing bancário "
        f"para o cliente {nome}, destacando a importância dos investimentos e o uso consciente do cartão."
    )
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
        )
        return response.text.strip()
    except Exception as e:
        print(f"Erro ao gerar mensagem para {nome}: {e}")
        return "Aproveite os benefícios exclusivos do seu cartão!"

print("Gerando mensagens personalizadas com Gemini...")
df["Mensagem"] = df["Nome"].apply(gerar_mensagem_marketing)

df.to_csv("dados_com_mensagens.csv", index=False)
print("Concluído! Arquivo dados_com_mensagens.csv gerado:")
print(df[["Nome", "Mensagem"]])
