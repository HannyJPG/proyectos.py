def chatbot_response(user_input):
    # Diccionario con palabras clave y respuestas
    responses = {
        "hola": "¡Hola! Bienvenido a nuestra empresa. ¿En qué puedo ayudarte?",
        "horario": "Nuestro horario de atención es de lunes a viernes, de 9:00 a 18:00 horas.",
        "direccion": "Estamos ubicados en Av. Principal 123, Ciudad Central.",
        "productos": "Ofrecemos servicios de software, desarrollo web y soluciones en la nube.",
        "contacto": "Puedes contactarnos al correo contacto@empresa.com o al teléfono +51 999 999 999.",
        "adios": "¡Gracias por tu visita! Que tengas un excelente día."
    }
    
    user_input = user_input.lower()  # Normalizar
    
    # Buscar palabra clave dentro de la frase del usuario
    for palabra_clave in responses:
        if palabra_clave in user_input:  # Si la palabra clave está en la frase
            return responses[palabra_clave]
    
    return "Lo siento, no entendí tu consulta. Intenta usar palabras como: horario, dirección, productos, contacto, adios."


# --- Menú inicial ---
print("🤖 Bienvenido al Chatbot Empresarial")
print("Puedes escribirme con frases naturales, pero reconoce estas palabras clave:")
print("👉 hola | horario | direccion | productos | contacto | adios")
print("Escribe 'adios' para salir.\n")

# --- Conversación ---
while True:
    user_input = input("Tú: ")
    respuesta = chatbot_response(user_input)
    print("Bot:", respuesta)
    
    if "adios" in user_input.lower():
        break