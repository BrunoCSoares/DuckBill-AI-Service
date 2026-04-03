import joblib
from flask import Flask, request, jsonify
import warnings

# Silenciar os avisos de versão para o terminal ficar limpo (opcional)
warnings.filterwarnings("ignore", category=UserWarning)

# 1. Inicializar o app Flask
app = Flask(__name__)

# 2. Carregamento do Pipeline
try:
    modelo_final = joblib.load('modelo_categorizador_bancario.pkl')
    print("🦆 DuckBill Engine: Modelo carregado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao carregar o modelo: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'description' not in data:
        return jsonify({"error": "Por favor, envie 'description' no JSON"}), 400
    
    descricao = data.get('description', '')

    # 3. Predição usando o pipeline
    try:
        # O pipeline já cuida do Tfidf + LogisticRegression
        categoria = modelo_final.predict([descricao.lower()])[0]
        probabilidade = modelo_final.predict_proba([descricao.lower()]).max()

        return jsonify({
            "description": descricao,
            "category": categoria,
            "confidence": round(float(probabilidade), 4),
            "status": "success"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- A PARTE QUE FALTOU ---
if __name__ == '__main__':
    # Roda o servidor na porta 5000
    print("🚀 Servidor DuckBill IA rodando em http://127.0.0.1:5000")
    app.run(debug=True, port=5000)