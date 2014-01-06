# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE
import time
import gettext
from gettext import gettext as _
gettext.textdomain('tic-tac-toe')

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('tic_tac_toe')

from tic_tac_toe_lib import Window
from tic_tac_toe.AboutTicTacToeDialog import AboutTicTacToeDialog
from tic_tac_toe.PreferencesTicTacToeDialog import PreferencesTicTacToeDialog

# See tic_tac_toe_lib.Window.py for more details about how this class works
class TicTacToeWindow(Window):
    __gtype_name__ = "TicTacToeWindow"
    global arr
    arr = []
    global flag
    flag = []
    global turn,count,check,endGame,win,Xn,On

    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(TicTacToeWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutTicTacToeDialog
        self.PreferencesDialog = PreferencesTicTacToeDialog

        # Code for other initialization actions should be added here.
        self.button1 = self.builder.get_object("button1")
        self.button2 = self.builder.get_object("button2")
        self.button3 = self.builder.get_object("button3")
        self.button4 = self.builder.get_object("button4")
        self.button5 = self.builder.get_object("button5")
        self.button6 = self.builder.get_object("button6")
        self.button7 = self.builder.get_object("button7")
        self.button8 = self.builder.get_object("button8")
        self.button9 = self.builder.get_object("button9")
        self.label = self.builder.get_object("label")
        self.entry = self.builder.get_object("entry")
        self.resetBtn = self.builder.get_object("resetBtn")
        self.msgLabel = self.builder.get_object("msgLabel")
        self.labelX = self.builder.get_object("labelX")
        self.labelO = self.builder.get_object("labelO")    
        global turn,count,arr,flag,win,Xn,On
        turn = 'x'
        count = 0
        Xn = 0
        On = 0
        win = 'd'
        arr = ['w','w','w','w','w','w','w','w','w']
        flag = [0,0,0,0,0,0,0,0,0]

    def on_resetBtn_clicked(self , widget):
        global turn,count,arr,flag,win,Xn,On
        if win=='x':
            self.msgLabel.set_text("X Won :D")
            Xn+=1
            self.labelX.set_text("X won: %d"%Xn)
        elif win=='o':
            On+=1
            self.labelO.set_text("O won : %d"%On) 
            self.msgLabel.set_text("O won :D")
        elif win=='d':
            self.msgLabel.set_text("Game Draw :|")
        turn = 'x'
        count = 0
        arr = ['w','w','w','w','w','w','w','w','w']
        flag = [0,0,0,0,0,0,0,0,0]
        self.button1.set_label("")
        self.button2.set_label("")
        self.button3.set_label("")
        self.button4.set_label("")
        self.button5.set_label("")
        self.button6.set_label("")
        self.button7.set_label("")
        self.button8.set_label("")
        self.button9.set_label("")
        self.label.set_text("X's Turn")

    def endGame():
        global flag
        flag = [1,1,1,1,1,1,1,1,1]

    def check():
        global count,win
        if (arr[0]==arr[1] and arr[2]==arr[0] and arr[0]=='x') or (arr[3]==arr[4] and arr[5]==arr[3] and arr[3]=='x') or (arr[6]==arr[7] and arr[8]==arr[6] and arr[6]=='x'):            
            #print 'X won horizontally'
            win='x'
            endGame()
        elif (arr[0]==arr[3] and arr[3]==arr[6] and arr[0]=='x') or (arr[1]==arr[4] and arr[4]==arr[7] and arr[1]=='x') or (arr[2]==arr[5] and arr[5]==arr[8] and arr[2]=='x'):
            #print 'X Won vertically'
            win='x'
            endGame()
        elif (arr[0]==arr[4] and arr[4]==arr[8] and arr[0]=='x') or (arr[2]==arr[4] and arr[4]==arr[6] and arr[2]=='x'):
            #print 'X won diagonally'
            win='x'
            endGame()
        elif (arr[0]==arr[1] and arr[2]==arr[0] and arr[0]=='o') or (arr[3]==arr[4] and arr[5]==arr[3] and arr[3]=='o') or (arr[6]==arr[7] and arr[8]==arr[6] and arr[6]=='o'):            
            #print 'O won horizontally'
            win='o'
            endGame()
        elif (arr[0]==arr[3] and arr[3]==arr[6] and arr[0]=='o') or (arr[1]==arr[4] and arr[4]==arr[7] and arr[1]=='o') or (arr[2]==arr[5] and arr[5]==arr[8] and arr[2]=='o'):
            #print 'O Won vertically'
            win='o'
            endGame()
        elif (arr[0]==arr[4] and arr[4]==arr[8] and arr[0]=='o') or (arr[2]==arr[4] and arr[4]==arr[6] and arr[2]=='o'):
            #print 'O won diagonally'
            win='o'
            endGame()
        else:
            if count==9:
                #print 'Its a Draw'
                win='d'
                endGame()
            else:
                return

    def on_button1_clicked(self, widget):
        global turn,count,arr,flag
        b=flag.pop(0)        
        if b!=1:
            self.msgLabel.set_text("Game Ongoing !")
            flag.insert(0,1)
            arr.pop(0)
            if turn == 'x' and count<9:
                widget.set_label("X")
                arr.insert(0,'x')
                turn='o'
                count += 1
                self.label.set_text("O's Turn")
            elif turn == 'o' and count<9:
                widget.set_label("O")
                arr.insert(0,'o')
                turn='x'
                count +=1
                self.label.set_text("X's Turn")
            if count==9:
                check() 
            check()
        else:
            flag.insert(0,1)
        

    def on_button2_clicked(self, widget):
        global turn,count,arr,flag
        b=flag.pop(1)        
        if b!=1:
            self.msgLabel.set_text("Game Ongoing !")
            flag.insert(1,1)
            arr.pop(1)
            if turn == 'x' and count<9:
                widget.set_label("X")
                arr.insert(1,'x')
                turn='o'
                count +=1
                self.label.set_text("O's Turn")
            elif turn == 'o' and count<9:
                widget.set_label("O")
                arr.insert(1,'o')
                turn='x'  
                count +=1
                self.label.set_text("X's Turn")
            if count==9:
                check() 
            check()
        else:
            flag.insert(1,1)

    def on_button3_clicked(self, widget):
        global turn,count,arr,flag
        b=flag.pop(2)        
        if b!=1:
            self.msgLabel.set_text("Game Ongoing !")
            flag.insert(2,1)
            arr.pop(2)
            if turn == 'x' and count<9:
                widget.set_label("X")
                arr.insert(2,'x')
                turn='o'
                count +=1
                self.label.set_text("O's Turn")
            elif turn == 'o' and count<9:
                widget.set_label("O")
                arr.insert(2,'o')
                turn='x'
                count+=1
                self.label.set_text("X's Turn")
            if count==9:
                check() 
            check()
        else:
            flag.insert(2,1)

    def on_button4_clicked(self, widget):
        global turn,count,arr,flag
        b=flag.pop(3)        
        if b!=1:
            self.msgLabel.set_text("Game Ongoing !")
            flag.insert(3,1)
            arr.pop(3)
            if turn == 'x' and count<9:
                widget.set_label("X")
                arr.insert(3,'x')
                turn='o'
                count+=1
                self.label.set_text("O's Turn")
            elif turn == 'o' and count<9:
                widget.set_label("O")
                arr.insert(3,'o')
                turn='x'  
                count+=1
                self.label.set_text("X's Turn")
            if count==9:
                check() 
            check()
        else:
            flag.insert(3,1)

    def on_button5_clicked(self, widget):
        global turn,count,arr,flag
        b=flag.pop(4)        
        if b!=1:
            self.msgLabel.set_text("Game Ongoing !")
            flag.insert(4,1)
            arr.pop(4)
            if turn == 'x' and count<9:
                widget.set_label("X")
                arr.insert(4,'x')
                turn='o'
                count+=1
                self.label.set_text("O's Turn")
            elif turn == 'o' and count<9:
                widget.set_label("O")
                arr.insert(4,'o')
                turn='x'  
                count+=1
                self.label.set_text("X's Turn")
            if count==9:
                check() 
            check()
        else:
            flag.insert(4,1)

    def on_button6_clicked(self, widget):
        global turn,count,arr,flag
        b=flag.pop(5)        
        if b!=1:
            self.msgLabel.set_text("Game Ongoing !")
            flag.insert(5,1)
            arr.pop(5)
            if turn == 'x' and count<9:
                widget.set_label("X")
                arr.insert(5,'x')
                turn='o'
                count+=1
                self.label.set_text("O's Turn")
            elif turn == 'o' and count<9:
                widget.set_label("O")
                arr.insert(5,'o')
                turn='x'
                count+=1
                self.label.set_text("X's Turn") 
            if count==9:
                check() 
            check()
        else:
            flag.insert(5,1)

    def on_button7_clicked(self, widget):
        global turn,count,arr,flag
        b=flag.pop(6)        
        if b!=1:
            self.msgLabel.set_text("Game Ongoing !")
            flag.insert(6,1)
            arr.pop(6)
            if turn == 'x' and count<9:
                widget.set_label("X")
                arr.insert(6,'x')
                turn='o'
                count+=1
                self.label.set_text("O's Turn")
            elif turn == 'o' and count<9:
                widget.set_label("O")
                arr.insert(6,'o')
                turn='x'
                count+=1
                self.label.set_text("X's Turn") 
            if count==9:
                check() 
            check()
        else:
            flag.insert(6,1)

    def on_button8_clicked(self, widget):
        global turn,count,arr,flag
        b=flag.pop(7)        
        if b!=1:
            self.msgLabel.set_text("Game Ongoing !")
            flag.insert(7,1)
            arr.pop(7)
            if turn == 'x' and count<9:
                widget.set_label("X")
                arr.insert(7,'x')
                turn='o'
                count+=1
                self.label.set_text("O's Turn")
            elif turn == 'o' and count<9:
                widget.set_label("O")
                arr.insert(7,'o')
                turn='x'
                count+=1 
                self.label.set_text("X's Turn")
            if count==9:
                check() 
            check()
        else:
            flag.insert(7,1)

    def on_button9_clicked(self, widget):
        global turn,count,arr,flag
        b=flag.pop(8)        
        if b!=1:
            self.msgLabel.set_text("Game Ongoing !")
            flag.insert(8,1)
            arr.pop(8)
            if turn == 'x' and count<9:
                widget.set_label("X")
                arr.insert(8,'x')
                turn='o'
                count+=1
                self.label.set_text("O's Turn")
            elif turn == 'o' and count<9:
                widget.set_label("O")
                arr.insert(8,'o')
                turn='x'  
                count+=1
                self.label.set_text("X's Turn")
            if count==9:
                check() 
            check()
        else:
            flag.insert(8,1)
