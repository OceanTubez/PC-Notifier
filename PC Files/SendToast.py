import webbrowser

from win10toast_click import ToastNotifier

toast = ToastNotifier()

toast.show_toast("Message Title", "Message Body", duration = 10)
