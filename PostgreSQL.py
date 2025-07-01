from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL
conn = psycopg2.connect("dbname=ai_application user=your_username password=your_password")

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT content
                FROM documents, 
                (SELECT pgai.vectorize(%s, 'openai-text-embedding-ada-002') AS query_vector) AS q
                ORDER BY embedding <=> query_vector
                LIMIT 5;
            """, (query,))
            results = cursor.fetchall()
        return render_template('results.html', results=results)

    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
