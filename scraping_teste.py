import requests
from bs4 import BeautifulSoup
import os


def get_news():
    url = "https://www.globo.com/"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # Encontrar todas as tags h2 com a classe "post__title"
    news_titles = soup.find_all("h2", class_="post__title")

    # Criar um dicionário para armazenar os títulos e os links das notícias
    news_dict = {}
    for title_tag in news_titles:
        # Extrair o texto do título
        title = title_tag.text.strip()
        # Encontrar o link associado ao título
        link_tag = title_tag.find_parent("a")
        if link_tag and "href" in link_tag.attrs:
            url = link_tag["href"]
            news_dict[title] = url

    return news_dict


# Chamar a função para obter as notícias
news = get_news()

# Exibir as notícias (se houver)
if news:
    for title, url in news.items():
        print(f"Title: {title}\nURL: {url}\n")
# Carregar variável de ambiente diretamente do sistema operacional
password = os.environ.get("PASSWORD")
if password is None:
    print("A senha não foi encontrada. Verifique suas configurações.")
    exit()  # ou qualquer outra ação apropriada, como lançar uma exceção

print(f"Variavel 1: {os.getenv('VARIAVEL1')}")
variavel = os.getenv("VARIAVEL1")

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance
msg = MIMEMultipart()

message = "Thank you"  # setup the parameters of the message

msg["From"] = "gabriellgonzaga@edu.unifil.br"
msg["To"] = "mario.adaniya@unifil.br"
msg["Subject"] = "[DS101] Teste de envio"

# add in the message body
msg.attach(MIMEText(message, "plain"))

# create server
server = smtplib.SMTP("smtp.gmail.com: 587")
server.starttls()

# Login Credentials for sending the mail
server.login(msg["From"], password)

# send the message via the server.
server.sendmail(msg["From"], msg["To"], msg.as_string())
server.quit()

print("successfully sent email to %s:" % (msg["To"]))
