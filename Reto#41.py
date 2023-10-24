import random, os

#    Este es un reto especial por Halloween.
#    Te encuentras explorando una mansión abandonada llena de habitaciones.
#    En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
#    Tu misión es encontrar la habitación de los dulces.
  
#    Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
#    (Tienes total libertad para ser creativo con los textos)
  
#    - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
#      que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
#      (16 habitaciones, siendo una de entrada y otra donde están los dulces)
#      Esta podría ser una representación:
#      🚪⬜️⬜️⬜️
#      ⬜️👻⬜️⬜️
#      ⬜️⬜️⬜️👻
#      ⬜️⬜️🍭⬜️
#    - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
#      Si no lo aciertas no podrás desplazarte.
#    - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
#      (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
#    - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
#    - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
#     tengas que responder dos preguntas para salir de ella.

def print_real_haunted_house():
    for x in range(DIMENSION):
        for y in range(DIMENSION):
            if (x,y) == candy_room:
                print("🍭", end=" ")
            elif (x,y) == entry:
                print("🚪", end=" ")
            elif (x,y) == first_ghost_room or (x,y) == second_ghost_room:
                print("👻" , end=" ")
            else:
                if (x,y) in haunted_house:
                    print("🔳", end=" ")
                else:
                    print("⬜️", end=" ")

        print("")

def print_player_haunted_house():
    for x in range(DIMENSION):
        for y in range(DIMENSION):
            if (x,y) == entry:
                print("🚪", end=" ")
            elif (x,y) == current_position and (x,y) != entry:
                print("🚹" , end= " ")
            elif  (x,y) in haunted_house:
                if (x,y) == first_ghost_room or (x,y) == second_ghost_room: 
                    print("👻" , end=" ")
                else:
                    print("🔳", end=" ")
            else:
                print("⬜️", end=" ")

        print("")

# Question generator system 
def get_question():
    next_question = random.randint(0, len(questions)-1)
    while used_question[next_question] == True:
        next_question = random.randint(0, len(questions)-1)

    used_question[next_question] = True
    return next_question


questions = [
    "¿En qué fecha se celebra Halloween?",
    "¿Qué fruta se utiliza comúnmente para tallar linternas en Halloween?",
    "¿Cuál es el nombre del villano en la película 'Viernes 13'?",
    "¿Cuál es el nombre de la festividad que sigue a Halloween y se celebra el 1 de noviembre?",
    "¿Qué animal es considerado un símbolo de Halloween?",
    "¿Cuál es el nombre de la famosa familia de monstruos en una serie de televisión de comedia?",
    "¿En qué país se originó la tradición de Halloween?",
    "¿Cuál es el nombre de la novela clásica de Bram Stoker que presenta a Drácula?",
    "¿Cuál es el nombre del pueblo de Nueva Inglaterra conocido por sus historias de brujería en el siglo XVII?",
    "¿Qué se supone que sucede si no se da 'truco o trato' en Halloween?",
    "¿Qué tipo de criatura es conocido por transformarse en un murciélago en la noche de Halloween?",
    "¿Qué Festividad Celta dió origen a Halloween?",
    "¿Cuál es el nombre del personaje principal en la película 'Pesadilla antes de Navidad'?",
    "¿Qué se dice que ocurre durante la noche de Halloween según la leyenda popular?",
    "¿Cuál es el nombre de la bruja que envenena a Blancanieves en el cuento de hadas?",
    "¿Cuál es el nombre de la famosa serie de películas de terror en la que un asesino enmascarado aterroriza a los adolescentes?",
    "¿Cuál es el nombre del evento en el que las personas visitan casas y reciben golosinas en Halloween?",
    "¿Qué palabra se utiliza para describir a un grupo de brujas?",
    "¿Qué objeto se utiliza para acabar con los vampiros en las historias de Halloween?",
    "¿Cómo se llama el terrorífico payaso que aparece en It, de Stephen King?",
    "¿Cuál es el nombre del pueblo donde tiene lugar la serie de televisión 'Stranger Things'?",
    "¿En qué año se estrenó la película 'Halloween' original?",
    "¿Qué color se asocia comúnmente con Halloween además del naranja?",
    "¿Cuál es el nombre de la canción popular que se asocia con Halloween y el famoso cantante Michael Jackson?",
    "¿Qué tipo de dulces son populares para distribuir en Halloween?"
] 
used_question = [False] * len(questions)
possible_answers = [
    "A. 31 de octubre\nB. 30 de octubre\nC. 1 de noviembre",
    "A. Calabaza\nB. Manzana\nC. Sandía",
    "A. Jason Voorhees\nB. Michael Myers\nC. Freddy Krueger",
    "A. Día de los Muertos\nB. Navidad\nC. Día de Todos los Santos",
    "A. Gato negro\nB. Perro\nC. Murciélago",
    "A. La Familia Adams\nB. La Familia Monster\nC. Los Locos Addams",
    "A. Estados Unidos\nB. Irlanda\nC. México",
    "A. Drácula\nB. Frankenstein\nC. El Fantasma de la Ópera",
    "A. Salem\nB. Sleepy Hollow\nC. Transilvania",
    "A. Se rompe un espejo\nB. Se cae una escalera\nC. Le cae una araña",
    "A. Hombre lobo\nB. Fantasma\nC. Vampiro",
    "A. Beltane \nB. Imbolc \nC. Samhain",
    "A. Jack Skellington\nB. Zero\nC. Sally",
    "A. Los muertos resucitan\nB. Los monstruos atacan\nC. Los espíritus aparecen",
    "A. Maléfica\nB. Úrsula\nC. Cruella de Vil",
    "A. Scream\nB. Saw\nC. The Purge",
    "A. Truco o trato\nB. Fiesta de disfraces\nC. Noche de miedo",
    "A. Jauría\nB. Akelarre\nC. Enjambre",
    "A. Crucifijo\nB. Ajo\nC. Estaca",
    "A. Percy Jackson\nB. Pennywise\nC. Peter",
    "A. Hawkins\nB. Derry\nC. Silent Hill",
    "A. 1976\nB. 1978\nC. 1980",
    "A. Violeta\nB. Amarillo\nC. Verde",
    "A. Ghostbusters \nB. Monster Mash\nC. Thriller",
    "A. Chocolate\nB. Regaliz\nC. Ositos Gominola"
]
solutions = ["A", "A", "A", "C", "C", "B", "B", "A", "A", "A", "C", "C", "A", "A", "B", "A", "A", "B", "C", "B", "A", "B", "A", "C", "A"]

# Define constants 
DIMENSION = 4

# Creating the house array
haunted_house = []
for x in range(DIMENSION):
    for y in range(DIMENSION):
        haunted_house.append((x, y))

# Choose randomly where the door will be 
entry = random.choice([(0,0),(0, DIMENSION-1), (DIMENSION-1, 0), (DIMENSION-1, DIMENSION-1)])
current_position = entry

# Define the candy room, far away from the door 
candy_room = entry
near = True
while candy_room == entry or near:
    candy_room = (random.randint(0,DIMENSION-1), random.randint(0,DIMENSION-1))
    if (abs(candy_room[0] - entry[0]) + abs(candy_room[1] - entry[1])) >= DIMENSION-1:
        near = False

# Create the phantasmagoric rooms and reset the haunted_house
haunted_house.remove(candy_room)
haunted_house.remove(entry)
first_ghost_room = random.choice(haunted_house)
haunted_house.remove(first_ghost_room)
second_ghost_room = random.choice(haunted_house)
haunted_house = []


correct_answer_messages = [
    "Menudo churro te has pegao, reconócelo.", 
    "No sé cómo lo has hecho... pero te estaré vigilando.", 
    "Vaya potra... vaya potra....", 
    "Has tenido suerte... por ahora.", 
    "Anda, tira... que no sé ni cómo has acertado eso.", 
    "Has buscado la respuesta en el ChatGPT, ¿Verdad?", 
    "Tu primo el friki te ha soplado la respuesta, seguro.", 
    "La suerte del principiante... Anda, tira, tira.", 
    "Te has salvado por los pelos, no sé ni cómo.", 
    "Vaya suerte macanuda que me llevas.", 
    "¿Cómo lo has hecho? Anda, sácate la chuleta del bolsillo, que te he visto."
]
welcome_message = """🧛‍♂️: ¡Oh! ¿Pero qué tenemos aquí? un valiente visitante ¡bienvenido a la Mansión Encantada 🏰! Me complace recibirte en este reino de misterios y enigmas. 
Soy Lestat, tu anfitrión en este viaje, un vampiro que ha vagado por estos pasillos encantados durante siglos.
Mi dominio está repleto de habitaciones misteriosas y desafíos desconcertantes. Tu objetivo es noble y claro: encontrar la habitación de los dulces para poder salir de la mansión. 
Sin embargo, para llegar allí, deberás enfrentarte a los secretos que guardan estas paredes ancestrales. 
No temas, querido huésped, te guiaré a través de esta aventura llena de emoción y suspense. Adelante, adéntrate en las sombras y deja que la valentía sea tu luz en la oscuridad."""
rules_message = """🧛‍♂️: Para superar cada una de las habitaciones deberás contestar con sabiduría a las cuestiones que se te planteen, solo entonces te dejaré avanzar entre habitaciones.
Pero ten mucho cuidado ya que esta increíble mansión está habitada por temerosos fantasmas, en caso de que te encuentres con uno de ellos también te propondrán una pregunta, por lo que deberás
acertar ambas"""
map_message = """🧛‍♂️: Aquí tienes el mapa de la mansión, ahora mismo te encuentras en la puerta (🚪). Después de cada turno deberás indicar hacia dónde quieres desplazarte,
las habitaciones son los cuadrados blancos (⬜️) ¡No intentes escaparte por las ventanas! Solo puedes salir encontrando la habitación dulce"""
scape_massage = """🧛‍♂️: ¿¡ESTÁS INTENTANDO ESCAPAR!? Nadie lo ha conseguido muchacho... Introduce una dirección correcta"""
question_messages = [
    "Muy bien... Acabas de entrar a esta habitación. Para poder avanzar a la siguiente debes responder correctamente a esta sencilla pregunta: ",
    "Estupendo. Has llegado a una nueva habitación. Responde correctamente a esta pregunta para avanzar: ",
    "¡Una nueva habitación te espera! Responde a esta pregunta para continuar: ",
    "Bienvenido a esta habitación desafiante. Responde esta pregunta para seguir adelante: ",
    "Otro desafío en esta habitación. Responde esta pregunta para avanzar: "
]
ghost_message = """👻: ¿A dónde vas tan rápido, acaso no te has dado cuenta que la habitación está gobernada por mí? ¿CÓMO QUE QUIÉN SOY YO? Soy el fantasma de Maria Carey y vengo a atormentarte 
hasta el 15 de enero. Contento me tienes... Si quieres que te deje avanzar debes responder a esta fantasmagórica pregunta: \n"""
candy_room_message = """🧛‍♂️: VAYA! Has encontrado la habitación de los caramelos 🍭 y podrás salir. Esta vez te me escapas... Pero vuelve cuando quieras. Este humilde servidor, Lestat, te estára esperando """
wrong_answer_message = """🧛‍♂️: MUAHAHAHAHA! Has perdido. Ahora serás presa de está mansión para siempre y me acompañarás guiando a otros insensatos como tú
🧑🏽: ¿Pero... Enserio? ¿Para toda la eternidad?
🧛‍♂️: Así es. A ver ese cuello muchacho llevo mucho tiempo sediento de sangre"""
# -----------------------------------------------------------------
# | Start of the game logic                                       |
# -----------------------------------------------------------------

os.system('cls')
print(welcome_message)
input("¿Aceptas el reto? (Presiona Enter para continuar...)")
os.system('cls')
print(rules_message)
input("(Presiona Enter para continuar...)")
os.system('cls')
print_player_haunted_house()
print(map_message)
input("(Presiona Enter para continuar...)")
os.system('cls')

# Start of the loop
while current_position != candy_room:
    os.system('cls')
    # till the movement is correct
    valid_movement = False
    while valid_movement != True:
        # Calculate movement
        directions_allowed = ["W", "w", "A", "a", "S", "s", "D", "d"]
        print_player_haunted_house()
        direction = input("¿Hacia dónde quieres moverte? Utiliza las letras W, A, S, D para indicar tu movimiento: ")
        while direction not in directions_allowed:
            direction = input("¿Hacia dónde quieres moverte? Utiliza las letras W, A, S, D para indicar tu movimiento: ")
        direction = direction.lower()

        # Check if correct 
        if direction == "w":
            if current_position[0]-1 >= 0:
                valid_movement = True
                current_position = (current_position[0]-1, current_position[1])
            else:
                print(scape_massage)
        elif direction == "s":
            if current_position[0]+1 <= DIMENSION-1:
                valid_movement = True
                current_position = (current_position[0]+1, current_position[1])
            else:
                print(scape_massage)
        elif direction == "a":
            if current_position[1]-1 >= 0:
                valid_movement = True
                current_position = (current_position[0], current_position[1]-1)
            else:
                print(scape_massage)
        elif direction == "d":
            if current_position[1]+1 <= DIMENSION-1:
                valid_movement = True
                current_position = (current_position[0], current_position[1]+1)
            else:
                print(scape_massage)

    # If the movement is correct, make a question
    if current_position != candy_room:
        os.system('cls')
        print_player_haunted_house()
        print(random.choice(question_messages))
        question_number = get_question()
        print(questions[question_number])
        print(possible_answers[question_number])
        user_answer = input("¿Cuál es tu respuesta?: ")
        if user_answer.upper() == solutions[question_number]:
            print("\n🧛‍♂️: " , random.choice(correct_answer_messages))
            haunted_house.append(current_position)
            input()
        else:
            print(wrong_answer_message)
            exit(0)

    # In case that you are in a ghost room, another question
    if current_position == first_ghost_room or current_position == second_ghost_room:
        os.system('cls')
        print_player_haunted_house()
        print(ghost_message)
        question_number = get_question()
        print(questions[question_number])
        print(possible_answers[question_number])
        user_answer = input("¿Cuál es tu respuesta?: ")
        if user_answer.upper() == solutions[question_number]:
            print("\n👻: " , random.choice(correct_answer_messages))
            haunted_house.append(current_position)
        else:
            print(wrong_answer_message)
            input('Presiona Enter para salir')
            exit(0)
# Repeat the loop till the player finds the candy room

# End of the game
os.system('cls')
print_real_haunted_house()
print(candy_room_message)
print("""
### ###  ### ###  ####       ####   ### ##            ###  ##    ##     ####     ####      ## ##   ##   ##  ### ###  ### ###  ###  ##
 ##  ##   ##  ##   ##         ##    ##  ##             ##  ##     ##     ##       ##      ##   ##  ##   ##   ##  ##   ##  ##    ## ##
 ##       ##       ##         ##       ##              ##  ##   ## ##    ##       ##      ##   ##  ##   ##   ##       ##       # ## #
 ## ##    ## ##    ##         ##      ##               ## ###   ##  ##   ##       ##      ##   ##  ## # ##   ## ##    ## ##    ## ##
 ##       ##       ##         ##     ##                ##  ##   ## ###   ##       ##      ##   ##  # ### #   ##       ##       ##  ##
 ##       ##  ##   ##  ##     ##    ##  ##             ##  ##   ##  ##   ##  ##   ##  ##  ##   ##   ## ##    ##  ##   ##  ##   ##  ##
####     ### ###  ### ###    ####   # ####            ###  ##  ###  ##  ### ###  ### ###   ## ##   ##   ##  ### ###  ### ###  ###  ##
""")
