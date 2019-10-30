from model.client import Client


def test_create_new_client(app):
    app.session.login(username="istomin.ev@gmail.com", password="Istomin18")
    app.create_new_client(Client("'English'", "name_field", "Legal_name_field", "primary_email_field",
                                 "Secondary_email_field", "Primary_phone_field", "secondary_phone_field",
                                 "fax_field", "78748", "country_field", "TX", "city_field"))
    app.session.logout()
