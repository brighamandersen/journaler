from flask import render_template, redirect, request, url_for
from models import JournalEntry
from config import app, db


@app.route("/")
def index():
    entries = JournalEntry.query.all()
    return render_template("index.html", entries=entries)


@app.route("/entry/<int:entry_id>")
def entry(entry_id):
    entry_to_display = JournalEntry.query.get(entry_id)
    return render_template("entry.html", entry=entry_to_display)


@app.route("/api/create-entry", methods=["POST"])
def api_create_entry():
    new_entry_content = request.form['new-entry-content']
    new_entry = JournalEntry(content=new_entry_content)
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/api/edit-entry", methods=["POST"])
def api_edit_entry():
    entry_id_to_edit = request.form['entry-id-to-edit']
    edit_entry_content = request.form['edit-entry-content']

    entry_to_edit = JournalEntry.query.get(entry_id_to_edit)
    entry_to_edit.content = edit_entry_content
    db.session.commit()
    return redirect(url_for('entry', entry_id=entry_id_to_edit))


@app.route("/api/delete-entry", methods=["POST"])
def api_delete_entry():
    entry_id_to_delete = request.form['entry-id-to-delete']
    entry_to_delete = JournalEntry.query.get(entry_id_to_delete)
    db.session.delete(entry_to_delete)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
