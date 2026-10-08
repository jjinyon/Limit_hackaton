from flask import Flask, jsonify, request
import api

app = Flask(__name__)
data = api.data

# 모든 아이템 조회
@app.route('/api/items')
def get_items():
    return jsonify([{"id": i, "text": item} for i, item in enumerate(ITEMS)])

# 새 아이템 추가
@app.route('/api/add-item', methods=['POST'])
def add_item():
    data = request.json
    ITEMS.append(str(data['text']))  # 단순 문자열 저장
    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)
