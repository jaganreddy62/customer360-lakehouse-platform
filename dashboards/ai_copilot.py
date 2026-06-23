import streamlit as st

from src.ai.prompt_builder import (
    build_prompt
)

from src.ai.sql_generator import (
    generate_sql
)

from src.ai.query_executor import (
    run_query
)

st.title("Customer360 AI Copilot")

question = st.text_input(
    "Ask a business question"
)

if st.button("Run"):

    prompt = build_prompt(question)

    sql = generate_sql(prompt)

    st.code(sql)

    result = run_query(sql)

    st.dataframe(result)