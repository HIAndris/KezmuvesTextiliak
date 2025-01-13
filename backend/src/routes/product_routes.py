from flask import Blueprint, jsonify
from src.models import Product

product_bp = Blueprint("products", __name__)

@product_bp.route("/", methods=["GET"])
def get_products():
    # Példa terméklista
    products = [
        {"id": 1, "name": "Laptop", "price": 1500},
        {"id": 2, "name": "Smartphone", "price": 800}
    ]
    return jsonify(products)
