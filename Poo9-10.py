class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "1. Precizarea modalitatilor de realizare a obiectivelor este un element de continut al functiei de: \na) previziune\nb) organizare\nc) cooronare\nRaspuns:",
     "\n2. Comunicarea si motivarea constituie suportul: \na)relatiilor intre manageri si executanti,\nb)functiei de cooronadre si antrenare\nc) subsistemului metodologic si decizional\nRaspuns:",
     "\n3. Strategiile economice se delimiteaza dupa criteriul: \na)dinamica obiectivelor\nb)natura obiectivelor si a principalelor abordari\nc) sfera de cuprindere\nRaspuns:",
     "\n4. Expresia <<Se refera la unul sau mai multe elemente de importanta pentru consumatori, ceea ce ii determina sa cumpere produsul sau serviciul respectiv>> este un element de caracterizare a: \na)obiectivelor strategice\nb)optiunilor strategice\nc)avantajului competitiv\nRaspuns:",
     "\n5. Factorii primari ai deciziei manageriale se afla printre elementele prezentate mai jos:\na)decidentul si mediul ambiant decizional\nb)decidentul si elementele endogene firmei care alcatuiesc situatia decizionala\nc)decidentul si elementele exogene firmei ce alcatuiesc situatia decizionala\nRaspuns:",
     "\n6. Care dintre elementele prezentate in continuare nu constituie cerinte de rationalitate pentru decizia de management:\na)fundamentarea stiintifica\nb)integrarea deciziei in ansamblul deciziilor firmei\nc)<<imputernicirea>> deciziei\nRaspuns:",
     "\n7. Diferenta dintre sistemul informational si sistemul informatic este data de:\na)existenta unor informatii specifice\nb)existenta unor circuite si fluxuri informationale mai scurte\nc)culegerea, transmiterea si prelucrarea cu mijloace automatizate a informatiilor\nRaspuns:",
     "\n8. Ce elemente definesc un post?\na)sarcinile, atributiile, lucrarile\nb)sarcinile, competentele, responsabilitatile\nc)sarcinile, activitatile, competentele\nRaspuns:",
     "\n9.Exista vreo diferenta intre post si functie, ca principale componente ale structurii organizatorice? \na)nu, pentru ca ambele sunt componente ale structurii organizatorice\nb)nu, este doar o deosebire terminologica\nc)da, pentru ca functia include mai multe posturi cu aceleasi caracteristici generale\nRaspuns:",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "c"),
     Question(question_prompts[3], "c"),
     Question(question_prompts[4], "a"),
     Question(question_prompts[5], "c"),
     Question(question_prompts[6], "a"),
     Question(question_prompts[7], "b"),
     Question(question_prompts[8], "a"),
]

def run_quiz(questions):
     punctaj = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               punctaj += 1
               nota=punctaj+1
     print("Ai obtinut", punctaj, "puncte din", len(questions),"+ 1 punct din oficiu = nota: ", nota)

run_quiz(questions)
