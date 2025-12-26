from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        "mssql+pyodbc://pinkyj81:zoskek38!!@ms1901.gabiadb.com/yujincast?"
        "driver=ODBC+Driver+17+for+SQL+Server"
    )
    # Keep idle connections from going stale; auto-reconnect on broken links.
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        "pool_pre_ping": True,   # ping before checkout to revive dropped connections
        "pool_recycle": 1800,    # recycle connections every 30 minutes
        "pool_timeout": 30,      # wait up to 30s for a connection
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False  # SQL 쿼리 로그 표시 여부
    db.init_app(app)
