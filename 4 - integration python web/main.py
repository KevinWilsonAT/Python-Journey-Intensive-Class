# 0a - ALWAYS USE    import flet as ft      BEFORE ANYTHING
# 0b - ALWAYS USE    def main(page):        TO START THE FILE
# 0c - ALWAYS USE    ft.app(target=main)    IN THE END OF THE FILE
# 0d - ALWAYS USE    page.update()          TO UPDATE THE APP APPEARANCE / INTERACTIVITY 


import flet as ft                   # 1a import flet to create app using the framework

def main(page):                     # 1b create main function of the app
    title = ft.Text("hashzap")      # 2a create Title Hashzap
    
    chat = ft.Column()              # 5a create chat

    def send_msg_tunnel(msg):                   # 7a create online interaction
        msg_text = ft.Text(msg)                 # 7d create a text with the msg
        chat.controls.append(msg_text)          # 7e set the text with the msg
        page.update()

    page.pubsub.subscribe(send_msg_tunnel)      # 7b set the online interaction

    def send_msg(event):                                                           # 5c send message on the chat
        page.pubsub.send_all(f"{popup_name_field.value}: {msg_field.value}")       # 7c send the msg for all users
        msg_field.value = ""                                                       # 6c clears the Text Field Message
        page.update()

    msg_field = ft.TextField(label="Insert message...", on_submit=send_msg)     # 5b create Text Field Message
    send_button = ft.ElevatedButton("Send", on_click=send_msg)                  # 5d create Button Send
    send_row = ft.Row([msg_field, send_button])                     # 6a create row "box" including [Text Field Message] and [Button Send]

    def enter_chat(event):                                                      # 4a the actions executed clicking on "Enter Chat"
        popup.open=False                                                        # 4b close popup
        page.remove(start_button)                                               # 4c remove Start Chat Button
        page.remove(title)                                                      # 4d remove title Hashzap
        page.add(chat)                                                          # 5e set chat
        page.pubsub.send_all(f"{popup_name_field.value} enters the chat")       # 7f create a text to inform someone enters the chat
        page.add(send_row)                                                      # 6b set row "box"
        page.update()

    popup_title = ft.Text("Welcome to Hashzap")                                # 3c Create Title Welcome to Hashzap
    popup_name_field = ft.TextField(label="Insert your name for the chat")     # 3d Create Text Field Insert your name for the chat
    popup_button = ft.ElevatedButton("Enter Chat", on_click=enter_chat)        # 3e Create Button Enter Chat

    popup = ft.AlertDialog(         # 3b create the popup
        open=False,                 # 3f set the popup to stay closed until clicked
        modal=True,                 # 3g set modal instead of popup
        title=popup_title,          # 3h set popup_title as the title
        content=popup_name_field,   # 3i set popup_name_field as the content
        actions=[popup_button]      # 3j set popup_button as the action
    )

    def open_popup(event):          # 3a popup / modal opening event
        page.dialog = popup
        popup.open = True
        page.update()

    start_button = ft.ElevatedButton("Start Chat", on_click=open_popup)  # 2c Button: Start Chat > Button clicked > call popup / modal

    page.add(title)                 # 2b adding title to the app
    page.add(start_button)          # 2c adding a button to the app

ft.app(target=main, view=ft.WEB_BROWSER)                 # 1c the calling of the app