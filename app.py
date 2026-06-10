from flask import Flask, render_template, request

app = Flask(__name__)

# 1. Ruta para la página principal (Home)
@app.route('/')
def home():
    return render_template('index.html')

# 2. Ruta para la página de la Galería
@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

# 3. Ruta que recibe los datos del formulario de contacto
@app.route('/enviar', methods=['POST'])
def enviar_mensaje():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    asunto = request.form.get('asunto')
    mensaje = request.form.get('mensaje')
    
    # Esto imprimirá los datos en tu terminal de VS Code para comprobar que el formulario funciona
    print(f"\n📩 ¡NUEVO CONTACTO DESDE LA WEB!")
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print(f"Asunto: {asunto}")
    print(f"Mensaje: {mensaje}\n")
    
    # Respuesta visual que verá el cliente
    return f"""
    <div style="text-align: center; font-family: Arial; padding: 50px;">
        <h1 style="color: #085041;">¡Gracias, {nombre}!</h1>
        <p style="font-size: 18px; color: #333;">Hemos recibido tu mensaje sobre '{asunto}' con éxito.</p>
        <p style="color: #555;">Un asesor técnico de BIOSAM S.A. se pondrá en contacto contigo pronto.</p>
        <br>
        <a href="/" style="background-color: #1D9E75; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Volver al Inicio</a>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True)