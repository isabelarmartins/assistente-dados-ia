import sqlite3

DB_PATH = "data/anexo_desafio_1.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def get_schema():
    conn = get_connection()
    cursor = conn.cursor()

    tabelas = ["clientes", "compras", "suporte", "campanhas_marketing"]
    schema_text = []

    for tabela in tabelas:
        cursor.execute(f"PRAGMA table_info({tabela});")
        colunas = cursor.fetchall()

        schema_text.append(f"Tabela: {tabela}")
        for coluna in colunas:
            nome_coluna = coluna[1]
            tipo_coluna = coluna[2]
            schema_text.append(f" - {nome_coluna} ({tipo_coluna})")

        cursor.execute(f"SELECT * FROM {tabela} LIMIT 3;")
        exemplos = cursor.fetchall()
        schema_text.append(" Exemplos:")
        for exemplo in exemplos:
            schema_text.append(f"   {exemplo}")

        schema_text.append("")

    conn.close()
    return "\n".join(schema_text)


def run_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    colunas = [desc[0] for desc in cursor.description] if cursor.description else []
    resultado = cursor.fetchall()
    conn.close()
    return colunas, resultado


def test_query(query):
    try:
        colunas, resultado = run_query(query)
        return {
            "success": True,
            "columns": colunas,
            "rows": resultado,
            "error": None,
        }
    except Exception as e:
        return {
            "success": False,
            "columns": [],
            "rows": [],
            "error": str(e),
        }