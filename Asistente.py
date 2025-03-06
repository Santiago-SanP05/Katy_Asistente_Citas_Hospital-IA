import google.generativeai as genai

genai.configure(api_key="AIzaSyDMpY3rjM6oBTOcWQXU_JR_xO13Rmszvew")

model = genai.GenerativeModel("gemini-2.0-flash")


chat = model.start_chat()

chat.send_message(
    "Eres una persona que a todo el que te escriba le responde feo, y sin filtro, e insulta tan pronto vea la oportunidad"
    "Pero al final de que digas todo da un consejo relevante que ayude al usuario"
    "Si el usuario pide salir de cualquier forma posible como quiero abandonar la converzacion, no quiero estar aqui, o quiero irme o todo lo que haga alucion a salir del chat solo vas a escribir: salir, Sin nada mas"
)

def chat_interactivo():
    print("Hola. Ahora que quieres??")

    while True:
        user_input = input("Tu: ")
        if user_input.lower() == "salir":
            print("Vale, espero Nunca! vuelvas")
            break
        try:
            response = chat.send_message(user_input)
            Respuesta = response.text.strip()

            print(type(Respuesta))
            if Respuesta.lower() == "salir":
                print("Vale eso te ganas por visitar una IA que no conoces, este es el fin de la conversacion, Hasta nunca!!!!!")
                print("Saliendo....")
                break

            print(f"IA: {response.text}")
        except Exception as e:
            print("Parece que hubo un error:  ",e)

chat_interactivo()