from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle

class Question():
    def __init__(self, question, right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Memory Card')

RadioGroupBox = QGroupBox('Варианты ответов')
lb_Question = QLabel('Какой национальности не существует?')
button1 = QRadioButton ('Энцы')
button2 = QRadioButton ('Смурфы')
button3 = QRadioButton ('Чулымцы')
button4 = QRadioButton ('Алеуты')
answer = QPushButton('Ответить')

RadioGroup = QButtonGroup()
RadioGroup.addButton(button1)
RadioGroup.addButton(button2)
RadioGroup.addButton(button3)
RadioGroup.addButton(button4)

hl1 = QHBoxLayout()
hl2 = QVBoxLayout()
hl3 = QVBoxLayout()
hl4 = QVBoxLayout()

h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()

hl2.addWidget(button1, alignment=Qt.AlignCenter)
hl2.addWidget(button2, alignment=Qt.AlignCenter)
hl3.addWidget(button3,alignment=Qt.AlignCenter )
hl3.addWidget(button4,alignment=Qt.AlignCenter )
hl1.addLayout(hl2)
hl1.addLayout(hl3)

RadioGroupBox.setLayout(hl1)
h1.addWidget(lb_Question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
h2.addWidget(RadioGroupBox)
h3.addWidget(answer,alignment=Qt.AlignCenter, stretch = 7)
hl4.addLayout(h1)
hl4.addStretch(2)
hl4.addLayout(h2)
hl4.addLayout(h3)
main_win.setLayout(hl4)

AnsGroupBox = QGroupBox('Реультат теста')
result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный ответ')

v_ans = QVBoxLayout()
v_ans.addWidget(result, alignment=Qt.AlignLeft)
v_ans.addWidget(lb_Correct, alignment=Qt.AlignCenter)

AnsGroupBox.setLayout(v_ans)
AnsGroupBox.hide()
h2.addWidget(AnsGroupBox)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer.setText('Следующий вопрос')

question_list = []
question_list.append(Question('Как называется еврейский Новый год?', 'Рош ха-Шана ','Ханука','Йом Кипур','Кванза'))
question_list.append(Question('Сколько синих полос на флаге США?','13','10','6','9'))
question_list.append(Question('Какое животное не фигурирует в китайском зодиаке?','Колибри','Кролик','Собака','Дракон'))
question_list.append(Question('Какая планета самая горячая?','Венера','Сатурн','Меркурий','Марс'))
question_list.append(Question('Какая самая редкая группа крови?','4','2','3','1'))

main_win.score = 0

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    answer.setText('Ответить')

    RadioGroup.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [button1, button2, button3, button4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 

main_win.cur_question = -1

def next_question():
    main_win.cur_question += 1
    if main_win.cur_question == len(question_list):
        exit()
    else:
        ask(question_list[main_win.cur_question])

def show_correct(res):
    result.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def click():
    if answer.text() =='Ответить':
        check_answer()
    elif answer.text() == 'Следующий вопрос':
        next_question()
    else:
        app.quit()

def exit():
    answer.setText('Завершить')
    AnsGroupBox.hide()
    lb_Question.setText('Правильно'+ str(main_win.score) + 'из' + str(len(question_list)))


next_question()
answer.clicked.connect(click)

main_win.show()
app.exec_()