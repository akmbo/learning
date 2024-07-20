from flask import Flask, render_template, redirect, request, flash
from contact_manager import ContactStore, Contact

app = Flask(__name__)
contact_store = ContactStore()

app.secret_key = "epic key"


@app.route("/")
def index():
    return redirect("/contacts")


@app.route("/contacts")
def contacts():
    search = request.args.get("q")
    if search is not None:
        found_contacts = contact_store.search(search)
    else:
        found_contacts = contact_store.contacts
    return render_template("index.html", contacts=found_contacts)


@app.route("/contacts/new", methods=["GET"])
def contacts_new_get():
    return render_template("new.html", contact=Contact())


@app.route("/contacts/new", methods=["POST"])
def contacts_new():
    c = Contact(
        None,
        request.form["first_name"],
        request.form["last_name"],
        request.form["phone"],
        request.form["email"],
    )
    if contact_store.save(c):
        flash("Created New Contact!")
        return redirect("/contacts")
    return render_template("new.html", contact=c)


@app.route("/contacts/<contact_id>")
def contacts_view(contact_id=0):
    contact = contact_store.find(contact_id)
    if contact is None:
        flash("Can't find contact")
        return redirect("/contacts")
    return render_template("show.html", contact=contact)


@app.route("/contacts/<contact_id>/edit", methods=["GET"])
def contacts_edit_get(contact_id=0):
    contact = contact_store.find(contact_id)
    if contact is None:
        flash("Can't find contact")
        return redirect("/contacts")
    return render_template("edit.html", contact=contact)


@app.route("/contacts/<contact_id>/edit", methods=["POST"])
def contacts_edit_post(contact_id=0):
    contact = contact_store.find(contact_id)

    contact.first = request.form["first_name"]
    contact.last = request.form["last_name"]
    contact.phone = request.form["phone"]
    contact.email = request.form["email"]
    # save to file

    flash("Updated Contact!")
    return redirect("/contacts")


@app.route("/contacts/<contact_id>/delete", methods=["POST"])
def contacts_delete(contact_id=0):
    if not contact_store.remove(contact_id):
        flash("Error While Deleting Contact.")
    else:
        flash("Deleted Contact!")
    return redirect("/contacts")
