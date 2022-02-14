
@app.route("/sqlinject/2", methods=["POST"])
def login():
    username = escape_string(request.form["username"])
    password = md5(request.form["password"]).digest().decode("latin-1")

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    selected_users = database.execute(query).fetchall()

    if len(selected_users) > 0:
        return "Login successful!"
    else:
        return "Incorrect username or password"