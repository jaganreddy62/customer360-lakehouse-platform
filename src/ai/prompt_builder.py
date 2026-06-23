def build_prompt(user_question):

    return f"""
You are a Snowflake SQL expert.

Schema:

CUSTOMER360
-----------
customer_id
customer_name
city
total_orders
total_spent
last_purchase_date

Generate only Snowflake SQL.

Question:
{user_question}
"""