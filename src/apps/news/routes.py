from src.apps.news import news_bp


@news_bp.route("/")
def news():
    ...
