import pygame
import time
import random
from tkinter import *
import setting as s

class GameGUI(Tk):
    '''
    GUI of the app
    '''
    def __init__(self) -> None:
        super().__init__()
        self.title('ScalePractice')
        self.config(s.WINDOW_CONFIG)
        self.play = Play()
        self.notes = [
            'C4',  
            'D4',
            'E4',
            'F4',
            'G4',
            'A4',
            'B4',
            'C5'   
        ]

        self.play_frame = Frame(self)
        self.play_frame.grid(row=0, column=0, sticky='ew')
        self.play_frame.config(bg=s.YELLOW)

        self.play_button = Button(self.play_frame, text="play",command=self.new_note)
        self.play_button.grid(column=0,row=0)
        self.play_button.config(bg=s.GREEN)

        self.replay_button = Button(self.play_frame,text="replay",command=self.play.replay_note)
        self.replay_button.grid(column=3,row=0)

        self.info_frame = Frame(self)
        self.info_frame.grid(row=1, column=0, sticky='ew')
        self.info_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.config(bg=s.YELLOW)

        self.show_info = Label(self.info_frame,text='press the corresponding key')
        self.show_info.grid(column=0,row=0,columnspan=5)
        self.show_info.config(bg=s.YELLOW)

        self.keys_frame = Frame(self)
        self.keys_frame.grid(row=2, column=0, sticky='ew')

        def create_note_buttons():
            for i, note in enumerate(self.notes):
                btn = Button(
                    self.keys_frame,
                    text=note,
                    command=lambda x=i: self.handel_click(x)
                )
                btn.grid(column=i, row=3)

        create_note_buttons()

        self.mainloop()

    def handel_click(self,index):
        label_text = self.play.check(index)
        self.show_info.config(text=label_text)
        pass

    def new_note(self):
        self.play.play_randon_note()
        self.show_info.config(text = 'try the correct key')


class Play:
    '''
    Play note and check anwser.
    '''
    def __init__(self) -> None:
        pygame.mixer.init()
        self.notes = [
            'C4',  
            'D4',
            'E4',
            'F4',
            'G4',
            'A4',
            'B4',
            'C5'   
        ]
        self.copy = self.notes * 2
        random.shuffle(self.copy)
        self.note_played = ''
        # play from C4 to C5 at initialization
        path = './source/test.wav'
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()


    def play_note(self,note):
        '''
        play a specific note
        '''
        try:
            note_name = note + '.wav'
            path = './source/'+ note_name
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            # wait till end playing
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
        except Exception as e:
            print(f"播放音符时出错: {e}")
    
    def play_randon_note(self):
        '''
        Play a random note
        '''
        if not self.copy:
            self.copy = self.notes * 2
            random.shuffle(self.copy)
        note = self.copy.pop()
        self.play_note(note)
        self.note_played = note

    def replay_note(self):
        '''
        Replay note
        '''
        self.play_note(self.note_played)

    def check(self,note_index_input):
        '''
        Check whether note input is correct note
        '''
        note_played_index = self.notes.index(self.note_played)
        self.play_note(self.notes[note_index_input])
        if note_played_index == note_index_input:
            label_text = 'correct! try play another one'
        else:
            label_text = 'wrong! try another key'
        return label_text

if __name__ == "__main__":
    ui = GameGUI()


