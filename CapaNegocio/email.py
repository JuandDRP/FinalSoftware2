class SenderEmail:
    def send_email(self, recipient_email, message_body, subject):
        print(f"[TEST] Simulando envío de email a {recipient_email}")
        print(f"[TEST] Asunto: {subject}")
        print(f"[TEST] Mensaje: {message_body}")