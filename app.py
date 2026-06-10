from flask import Flask, render_template, request
import smtplib
import ssl
from email.message import EmailMessage
import os

app = Flask(__name__)

# 1. Ruta para la página principal (Home)
@app.route('/')
def home():
    return render_template('index.html')

# 2. Ruta para la página de la Galería
@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

# 3. Ruta que recibe y ENVÍA los datos del formulario de contacto
@app.route('/enviar', methods=['POST'])
def enviar_mensaje():
    # Recolectamos la información del cliente
    nombre = request.form.get('nombre')
    email_cliente = request.form.get('email')
    asunto = request.form.get('asunto')
    mensaje = request.form.get('mensaje')
    
    # Buscamos las llaves en la caja fuerte del servidor (Render)
    mi_correo = os.environ.get('EMAIL_USUARIO')
    mi_password = os.environ.get('EMAIL_PASSWORD')
    
    # Preparamos el correo electrónico
    msg = EmailMessage()
    msg['Subject'] = f"🔔 NUEVO CONTACTO WEB BIOSAM: {asunto}"
    msg['From'] = mi_correo
    msg['To'] = mi_correo # Te lo envías a ti mismo
    
    # Diseñamos el texto que te llegará a ti
    msg.set_content(f"""
    ¡Hola! Tienes un nuevo mensaje desde la página web de BIOSAM:

    DATOS DEL CLIENTE:
    -------------------
    Nombre: {nombre}
    Correo: {email_cliente}
    Asunto: {asunto}

    MENSAJE:
    -------------------
    {mensaje}
    """)
    
    # Encendemos el motor de envío de forma segura
    try:
        if mi_correo and mi_password:
            contexto_seguro = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto_seguro) as smtp:
                smtp.login(mi_correo, mi_password)
                smtp.send_message(msg)
            print("✅ Correo enviado a tu bandeja con éxito.")
        else:
            print("⚠️ Faltan las llaves en la caja fuerte del servidor.")
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")
    
    # Respuesta visual que verá el cliente en la página
    return f"""
    <div style="text-align: center; font-family: Arial; padding: 50px;">
        <h1 style="color: #085041;">¡Gracias, {nombre}!</h1>
        <p style="font-size: 18px; color: #333;">Hemos recibido tu mensaje sobre '{asunto}' con éxito.</p>
        <p style="color: #555;">Un asesor técnico de BIOSAM se pondrá en contacto contigo muy pronto.</p>
        <br>
        <a href="/" style="background-color: #1D9E75; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Volver al Inicio</a>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True)