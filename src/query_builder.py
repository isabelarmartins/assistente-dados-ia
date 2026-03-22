def build_prompt(pergunta, schema):
    return f"""
Você é um especialista em SQL para SQLite.

Seu trabalho é converter perguntas em linguagem natural em uma query SQL válida.

Regras:
- Use apenas tabelas e colunas existentes no schema.
- Gere apenas SQL, sem explicações.
- Use sintaxe compatível com SQLite.
- Se a pergunta envolver datas, considere que os campos de data estão em formato YYYY-MM-DD.
- Prefira respostas agregadas quando a pergunta pedir contagens, médias, totais ou tendências.
- Nunca invente colunas.

Schema do banco:
{schema}

Pergunta do usuário:
{pergunta}

Retorne somente a query SQL.
""".strip()