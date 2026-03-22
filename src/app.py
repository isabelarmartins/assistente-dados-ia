import streamlit as st
import pandas as pd
from db_utils import get_schema, test_query
from query_builder import build_prompt
from llm_service import generate_sql

st.title("🤖 Assistente Inteligente de Análise de Dados")
st.write("Faça perguntas sobre clientes, compras, suporte ou campanhas.")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    schema = get_schema()
    prompt = build_prompt(pergunta, schema)

    with st.spinner("Gerando resposta com IA..."):
        sql = generate_sql(prompt)

    # SQL escondida (expander)
    with st.expander("🧠 Ver SQL gerada"):
        st.code(sql, language="sql")

    resultado = test_query(sql)

    if resultado["success"]:
        st.subheader("📊 Resultado:")

        df = pd.DataFrame(
            resultado["rows"],
            columns=resultado["columns"]
        )

        st.dataframe(df)

        # só mostra gráfico se fizer sentido
        if len(df.columns) >= 2 and len(df) > 1:
            try:
                st.subheader("📈 Gráfico:")
                st.bar_chart(df.set_index(df.columns[0]))
            except Exception:
                pass

    else:
        st.error(f"Erro ao executar a query: {resultado['error']}")