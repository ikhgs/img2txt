from flask import Flask, request, jsonify
import replicate

app = Flask(__name__)

@app.route('/', methods=['GET'])
def extract_text():
    # Récupérer l'URL de l'image à partir des paramètres de requête
    image_url = request.args.get('image')

    if not image_url:
        return jsonify({"error": "L'URL de l'image est requise."}), 400

    try:
        output = replicate.run(
            "abiruyt/text-extract-ocr:a524caeaa23495bc9edc805ab08ab5fe943afd3febed884a4f3747aa32e9cd61",
            input={
                "image": image_url
            }
        )
        return jsonify({"text": output}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
