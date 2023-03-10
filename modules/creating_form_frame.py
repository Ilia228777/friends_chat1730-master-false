import customtkinter
import modules.button_send as m_button
import modules.screen_app as m_app
import modules.create_frame as m_frame

class MessageFrame(m_app.App):
    def __init__(self, app_width, app_height, **kwargs):
        super().__init__(app_width =  app_width, app_height = app_height, **kwargs)
        self.FRAME_MESSAGE = m_frame.My_Frame(text="Василь", master=self, width=520 // 2, height= app_height - 125 // 2, border_width=6)
        self.FRAME_MESSAGE.grid(row=0, column=2, padx=5, pady=10, sticky=customtkinter.N)

main_app = MessageFrame(800, 600)