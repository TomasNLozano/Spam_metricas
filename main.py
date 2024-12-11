import schedule
import time
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from env import APP_PASSWORD, SENDER, RECIPIENTS_1, RECIPIENTS_2, RECIPIENTS_3, SUBJECT_FROM

subject = 'Status de sprint - ' + SUBJECT_FROM
recipients = [RECIPIENTS_1,RECIPIENTS_2,RECIPIENTS_3]
body = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estado del Sprint</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            background-color: #f9f9f9;
        }
        h1, h2 {
            color: #333;
        }
        p {
            color: #555;
        }
        .footer {
            margin-top: 20px;
            font-size: 0.9em;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Estado Actual del Sprint</h1>
        <p>Estimados,</p>
        <p>
            Me permito compartirles una breve actualización sobre el estado actual del sprint. 
            En este momento, todo se encuentra bien y las tareas planificadas están siendo resueltas 
            conforme al cronograma establecido. Además, las reuniones previstas se han coordinado 
            acorde a las necesidades y se están llevando a cabo de manera efectiva.
        </p>
        <p>
            Espero que de su lado también todo esté en orden y que los planes definidos para el sprint 
            avancen de acuerdo a lo esperado.
        </p>
        <p class="footer">
            Saludos cordiales, estimados, y quedo al pendiente ante cualquier duda o consulta.
        </p>
    </div>
</body>
</html>
"""

def check_dia_laboral():
    dia_actual = datetime.now().weekday()
    if dia_actual in range(0, 5):
        send_email()

def send_email():
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = SENDER
    msg['To'] = ','.join(recipients)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(SENDER, APP_PASSWORD)
        smtp_server.sendmail(SENDER, recipients, msg.as_string())

check_dia_laboral()
check_dia_laboral()
check_dia_laboral()
check_dia_laboral()

# schedule.every().day.at("09:00").do(check_dia_laboral)
# schedule.every().day.at("12:00").do(check_dia_laboral)
# schedule.every().day.at("15:00").do(check_dia_laboral)
# schedule.every().day.at("18:00").do(check_dia_laboral)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
