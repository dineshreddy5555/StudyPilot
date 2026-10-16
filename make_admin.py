from database import get_connection, create_tables

create_tables()

email = input("Enter your registered StudyPilot email: ").strip().lower()

connection = get_connection()

try:
    user = connection.execute(
        "SELECT id, username, email, is_admin FROM users WHERE email = ?",
        (email,)
    ).fetchone()

    if user is None:
        print("Account not found. Register this account first.")
    else:
        connection.execute(
            "UPDATE users SET is_admin = 1 WHERE id = ?",
            (user["id"],)
        )
        connection.commit()

        print("Admin access enabled successfully!")
        print("Username:", user["username"])
        print("Admin:", True)

finally:
    connection.close()




