from db_utils import get_schema, test_query
from query_builder import build_prompt
from llm_service import generate_sql

if __name__ == "__main__":
    pergunta = input("Digite sua pergunta: ")

    schema = get_schema()
    prompt = build_prompt(pergunta, schema)

    print("\nGerando SQL com IA...")

    sql = generate_sql(prompt)

    print("\nSQL GERADA:")
    print(sql)

    resultado = test_query(sql)

    print("\nRESULTADO:")
    print(resultado)