from src.routes.product_routes import product_bp

def register_routes(app):
    app.register_blueprint(product_bp, url_prefix="/api/products")
