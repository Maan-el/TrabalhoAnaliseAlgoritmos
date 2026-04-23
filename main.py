from tkinter import messagebox, simpledialog
from comparator import Comparator
from notifier import Notify
from scheduler import Schedule
from selector import Selection
from validator import Validator

# testando as coisas

input_usr: str = ""
validator = Validator()

tmp_input_usr = simpledialog.askstring("Website", "Cole aqui a url que será monitorada")
input_usr = tmp_input_usr if tmp_input_usr is not None else ""

if not validator.is_url(input_usr):
    messagebox.showerror("Error", "URL inválida")
    quit()

# tmpinput = "https://impostometro.com.br/"
# url = input("Cole aqui a url que será monitorada:")
# s = Selection(tmpinput)

s = Selection(input_usr)
notifier = Notify()
comparator = Comparator(s, notifier, 1)
print()
print(comparator)

schedule = Schedule()
schedule.start(comparator)
while True:
    x = input()
    if x != "":
        schedule.stop()
        break
