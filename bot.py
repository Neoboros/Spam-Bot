from instapy2 import InstaPy2

login = input("Usuário do BOT: ")
passwd = input("Senha do BOT: ")
username = input("Nome do Perfil: ")
comment = input("Comentário: ")

session = InstaPy2()
session.login(username = login, password = passwd)

session.configuration.comments.set_enabled(enabled=True)
session.configuration.likes.set_enabled(enabled=True)
session.configuration.comments.set_comments(comments=[
    comment
])
session.configuration.comments.set_percentage(percentage=100)
session.configuration.likes.set_percentage(percentage=100)
session.interact_users(amount=50, usernames=[username], randomize_media=True)

