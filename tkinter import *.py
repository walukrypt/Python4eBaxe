from tkinter import *
from random import choice
from random import shuffle


root = Tk()
root.title('MajasWotdFlip')
root.geometry("600x400+-1900+100")


my_label = Label(root, text="", font=("Helvetica", 48))
my_label.pack(pady=20)

def shuffler():
    # Clear Hint Label 
    hint_label.config(text='')

    # Clear Hint Count
    global hint_count
    hint_count = 0

    # Clear Answer Box
    entry_answer.delete(0, END)

    # Clear Answer Label
    answer_label.config(text='')

    # List of state words
    states = ['Bawo ni?', 'No gonda?', 'Ẹ káàárọ̀ ','Jam tan','Ẹ káàsán', 'Jam wodi', 'Ẹ káalẹ́ ', 'Jam na foti', 'kúùjọkòó', 'No foti', 'Ẹ sé' , 'Ajaraama', 'Jọ̀ọ́ ', 'Jam aada', 'Mo ní fẹ́ ,  'Mi yewi', 'Báwo ni orúkọ rẹ?', 'No honto?', 'Orúkọ mi ni', 'Mi honto', 'Ọmọ', 'Baajo', 'Bàbá', 'Baaba', 'Màmá', 'Ndewo', 'Ẹ̀gbọ́n', 'Sedyo', 'Àbúrò', 'Gorko', 'Ọkùnrin', 'Naado', 'Obìnrin', 'Debbo', 'Ile', 'Wuro', 'Ilé ìwé', 'Daande', 'Ounje', 'Lewru', 'Òrò', 'Konngi', 'Omi', 'Ndiyam', 'Ẹbọ', 'Seeri', 'Ẹyin', 'Noowo', 'Isu', 'Ndiiw', 'Ẹran', 'Leela', 'Àṣọ', 'Daani', 'Ijò' , 'Daali', 'Igbẹ́ ', 'Seero', 'Ìgbẹ́ ', 'Leesi', 'Ọ̀dọ', 'Lawol', 'Ọ̀yà', 'Jamu', 'Moun', 'Òṣùpá', 'Lewru',  'Òun tímo fẹ́ ', 'Mi yewi', 'Ìròyìn', 'Hareey','Ọ̀rọ̀ tí ó ṣẹlẹ̀', 'Gorko', 'gbẹ́sẹ̀ ', 'Fott', 'Ète', 'Pulaar', 'Orí', 'Honto', 'ẹranko', 'Naado leela', 'Ẹṣin', 'Hiima', 'Iná' , 'Fire', 'Òtútù', 'Ngella', 'Òjò', 'Ruwa', 'Ìrìnàjò', 'Yellagol', 'Ẹ̀gbọ́n', 'Noddle', 'Ilé Ìgbéyàwó', 'Daande', 'marwo', 'Ìrẹ́jẹ', 'Lehru', 'Ẹsẹ́ ', 'Wale', 'Ìsọ́ra', 'Jam', 'Ẹ́lẹ́dàa', 'Mooso', 'Iwọ', 'Aadi', 'Ẹgbọ́n tímo fẹ́', 'Gorko yewi', 'Olúwa', 'Allah', 'Ilé iṣẹ́ ', 'Taare', 'Àṣá', 'Konngi', 'Ìjọba', 'Beegi', 'Ìlú', 'Dekkere', 'Ẹwá',' Deena', 'Oríkì', 'Wale', 'Àkọ́kọ́ ', 'Fettunde', 'Àtijọ', 'Daaɗi', 'Ìjẹ́wẹ̀ ', 'Luudo', 'Ojú', 'Wana', 'Ọgbọ́n', 'Siina', 'Ọgbọ́n tímo ní', 'Mi siina', 'Ìlu'', 'Wuro', 'Ìfẹ́ ', 'Habbere', 'Ọ̀rẹ́ ', 'Maro', 'Òun tímo nse', 'Mi noggi', 'Orí ẹ̀yìn', 'Wani laawol', 'Ilé Ìgbéyàwó', 'Daande marwo', 'Igbéyàwo', 'Ndoorti', 'Ìjọba', 'Beegi' , 'Ìlú', 'Wuro', 'Àìní', 'Weeti', 'Ọkùnrin tímo ní', 'Mi naado',  'Obìnrin tímo ní', 'Mi debbo', 'Èda', 'Mooso', 'Òun tímo ní', 'Miɗo', 'Igi', 'Ndow', 'Ìfẹ́ ', 'Habbere', 'Ẹ̀jẹ́ ', 'Dentu', 'Orí', 'Wano', 'Ẹnu', 'Pene', 'Orí', 'Wana', 'Ẹ̀gbọ́n', 'tímo fẹ́ ', 'Gorko yewi', 'Ile', 'Wuro', 'Ọ̀dọ̀ ', 'Lewol', 'Òṣùpá', 'Lewru', 'Iná', 'Leela', 'Ìrìnàjò','Yellagol', 'Ẹ̀ṣẹ́ ', 'Wale', 'Oregon', 'California', 'Ohio', 'Nebraska', 'Colorado', 'Michigan', 'Massachusetts', 'Florida', 'Texas', 'Oklahoma', 'Hawaii', 'Alaska', 'Utah', 'New Mexico', 'North Dakota', 'South Dakota', 'West Virginia', 'Virginia', 'New Jersey', 'Minnesota', 'Illinois', 'Indiana', 'Kentucky', 'Tennessee', 'Georgia', 'Alabama', 'Mississippi', 'North Carolina', 'South Carolina', 'Maine', 'Vermont', 'New Hampshire', 'Connecticut', 'Rhode Island', 'Wyoming', 'Montana', 'Kansas', 'Iowa', 'Pennsylvania', 'Maryland', 'Missouri', 'Arizona', 'Nevada', 'New York', 'Wisconsin', 'Delaware', 'Idaho', 'Arkansas', 'Louisiana']
    # Pick random state from list
    global word
    word = choice(states)
    

    # Break apart our chosen word
    break_apart_word = list(word)
    shuffle(break_apart_word)
    
    # Turn shuffeled List into a word
    global shuffled_word
    shuffled_word =  ''
    for letter in break_apart_word:
        shuffled_word += letter
    
    # print shuffled word to the screen
    my_label.config(text=shuffled_word)

#Create answer Function
def answer():
    if word == entry_answer.get():
        answer_label.config(text="Correct!!")
    else:
        answer_label.config(text="Incorrect!!")

# Create Hint Counter
global hint_count
hint_count = 0

# Create Hint Function
def hint(count):
    global hint_count
    hint_count = count

    # Get the length of the chosen word
    word_length = len(word)

    # Show Hint
    if count < word_length:
        hint_label.config(text=f'{hint_label["text"]} {word[count]}')
        hint_count +=1 

entry_answer = Entry(root, font=("Helvetica", 24))
entry_answer.pack(pady=20)


button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=10)

my_button = Button(button_frame, text="Pick Another Word", command=shuffler)
my_button.grid(row=0, column=1, padx=10)

hint_button = Button(button_frame, text="Hint", command=lambda: hint(hint_count))
hint_button.grid(row=0, column=2, padx=10)


answer_label = Label(root, text='', font=("Helvetica", 18))
answer_label.pack(pady=20)

hint_label = Label(root, text='', font=("Helvetica", 18))
hint_label.pack(pady=10)

shuffler()
root.mainloop()''