from db import db
from flask import session, render_template
import users

def send(content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO feedback (content, sent_at) VALUES (:content,NOW())"
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return True

