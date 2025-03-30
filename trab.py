import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(destinatario, assunto, mensagem):
    remetente = "seu_email@gmail.com"  
    senha = "sua_senha" 

    
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remetente, senha)

    
    email = MIMEMultipart()
    email['From'] = remetente
    email['To'] = destinatario
    email['Subject'] = assunto
    email.attach(MIMEText(mensagem, 'plain'))

    
    servidor.sendmail(remetente, destinatario, email.as_string())
    servidor.quit()

    print("E-mail enviado com sucesso!")


destinatario = "destinatario_email@gmail.com"
assunto = "Contato do Formulário de Monique"
mensagem = "Olá, gostaria de entrar em contato para discutir sobre um projeto."
enviar_email(destinatario, assunto, mensagem)