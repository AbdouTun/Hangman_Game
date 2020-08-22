from tkinter import *
import json
from pygame import mixer
import data
from random import randint
import time
cas = False
mixer.init()
mixer.music.load("./Data/music/alan_walker_daytime.mp3")
t = 40
esm_eli_9a3d_yal3b = ''
elkelma = ''
elkelmato_ = ''
kelma_ = ''
score = 0
chance = 6
findch = []
class entry(Frame):
    def __init__(self,app,ax,ay):
        Frame.__init__(self,app)
        return (Entry(app).place(x=ax,y=ay))
    def ins(self):
        self.input.insert(0,x)
class lbl(Frame):
    def __init__(self,app,txt,f,ax,ay):
        Frame.__init__(self,app)
        if isinstance(txt,StringVar):
            return Label(app,textvariable=txt,font=f,bg = "#000",fg = "#999").place(x=ax,y=ay)
        else :
            return Label(app,text=txt,font=f,bg = "#000",fg = "#999").place(x=ax,y=ay)
class btn(Frame):
    def __init__(self,app,txt,ax,ay,f,color,bgcolor,cmd,w,h):
        Frame.__init__(self,app)
        if isinstance(txt,StringVar):
            return(Button(app, textvariable=txt,fg=color,bg=bgcolor,font=f,command=cmd).place(x=ax,y=ay,width=w,height=h))
        else:
            return(Button(app, text=txt,fg=color,bg=bgcolor,font=f,command=cmd).place(x=ax,y=ay,width=w,height=h))

class cnvs(Frame):
    def __init__(self,app,ax,ay,img_src):
        Frame.__init__(self,app)
        self.img = PhotoImage(file=img_src)
        self.canvas = Canvas(app,width=665,height=380,bg="#333")
        self.canvas.create_image((330, 185), image = self.img)
        self.canvas.place(x=ax,y=ay)

class playName(Frame):
    def back(self,frm):
        frm.show_frame(start)
    def __init__(self,frm ):
        Frame.__init__(self,frm)
        self.cnvs = cnvs(frm,-1,-1,"./Data/backgrounds/start.png")
        self.lbl = lbl(frm,"Votre Nom ",("arial",16,"bold"),255,115)
        self.name = Entry(frm,font = ('verdana',10,'bold'))
        self.name.place(x=230,y=162,width = 167,height = 30)
        self.jouer = btn(frm,"Commencer",230,200,('verdana',12,'bold'),"white","#0752FF",lambda: self.commencer(frm),167,35)
        self.photo = PhotoImage(file = "./Data/backgrounds/back.png") 
        self.backbtn = Button(frm,image = self.photo,command=lambda : self.back(frm))
        self.backbtn.config(bg='#0ad200')
        self.backbtn.place(x=3,y=3)
    def commencer(self,frm):
        if self.name.get().isalpha():
            global esm_eli_9a3d_yal3b
            esm_eli_9a3d_yal3b = self.name.get()
            games.startGame()
            frm.show_frame(engame)
        else:
            import tkinter.messagebox
            tkinter.messagebox.showerror('Invalid Nom', "Saisir Votre Nom Correct!!")
        

class engame(Frame):
    def check(self,i):
        global score,chance,t
        if not games.findch(self.chr[i].cget("text")):
            chance -= 1
            self.chnc = StringVar()
            self.chnc.set("Vous Avez \n {} \n Chances".format(chance))
            if chance <6 and chance >4:
                color = self.green
            elif chance <5 and chance >2:
                color = self.yellow
            elif chance <3 :
                color = self.red
            self.chance = Label(self.frm,textvariable = self.chnc,font = ("times",14,"bold"),bg="#000",fg=color)
            self.chance.place(x=495,y=135)
            self.click += 1
            self.img = PhotoImage(file = self.imgs[self.click]) 
            self.pendu.config(image = self.img)
        else:

            score += chance*t
        games.findch(self.chr[i].cget("text"))
        global kelma_,elkelma
        self.txt.set(kelma_)
        self.psc = Label(self.frm,textvariable = self.txt,font = ("times",17,"bold"))
        self.chr[i].destroy()
        if kelma_.replace(' ','') == elkelma:
            self.txt = StringVar()
            self.txt.set(elkelma)
            self.psc = Label(self.frm,textvariable = self.txt,font = ("times",17,"bold"))
            self.pwin()
        if chance == 0:
            self.plose()
    def back(self,frm):
        global t,cas
        t = -2
        cas = True
        self.timer.destroy()
        self.frm.show_frame(playName)
    def pwin(self):
        self.frm.show_frame(win)
    def plose(self):
        self.frm.show_frame(lose)

    def countdown(self,tm):
        global t,kelma_,elkelma,chance,cas
        t=tm
        if not cas and t != -2 :
            if chance == 0 :
                return 0
            if t > -1 and kelma_.replace(' ','') != elkelma:
                self.time.set(t)
                if t <=40 and t>=25 :
                    self.color = self.green
                elif t<25 and t>=10 :
                    self.color = self.yellow
                else :
                    self.color = self.red
                    self.time.set('0'+str(t))
                self.timer = Label(self.frm,textvariable = self.time,font = ("times",25,"bold"),fg=self.color,bg="#000")
                self.timer.place(x=595,y=23)
                self.frm.after(1000, self.countdown, t-1)
            elif t == -1 and kelma_.replace(' ','') != elkelma:
                self.plose()
        else :
            self.timer.destroy()
    def __init__(self,frm ):
        Frame.__init__(self,frm )
        global t
        self.frm = frm
        self.click = 0
        self.yellow = '#FFDB00'
        self.green = '#0BE600'
        self.red = 'red'
        self.color = ''
        self.imgs = ['./Data/man/l0.png','./Data/man/l1.png','./Data/man/l2.png','./Data/man/l3.png','./Data/man/l4.png','./Data/man/l5.png','./Data/man/l6.png']
        self.cnvs = cnvs(frm,-1,-1,"./Data/backgrounds/engame.png")
        global esm_eli_9a3d_yal3b
        self.tx = StringVar()
        self.tx.set('Tunisie Gouvernantes')
        self.title = Label(frm,textvariable = self.tx,font = ("times",25,"bold"),fg='red',bg="#000")
        self.title.place(x=102,y=0,width = 470,height = 80)
        self.time = StringVar()
        self.time.set(t)
        self.timer = Label(self.frm,textvariable = self.time,font = ("times",25,"bold"),fg=self.green,bg="#000")
        self.timer.place(x=595,y=23)
        self.countdown(40)
        self.img = PhotoImage(file = self.imgs[self.click]) 
        self.pendu = Label(frm,image = self.img)
        self.pendu.place(x=25,y=105)
        self.photo = PhotoImage(file='./Data/backgrounds/back.png')
        self.backbtn = Button(frm,image = self.photo,command=lambda : self.back(frm))
        self.backbtn.config(bg='#0ad200')
        self.backbtn.place(x=3,y=3)
        global kelma_
        self.txt = StringVar()
        self.txt.set(kelma_)
        self.psc = Label(self.frm,textvariable = self.txt,font = ("times",17,"bold"))
        self.psc.place(x=200,y=140, width=200,height=50)
        global chance
        self.chnc = StringVar()
        self.chnc.set("Vous Avez \n {} \n Chances".format(chance))
        self.chance = Label(self.frm,textvariable = self.chnc,font = ("times",14,"bold"),bg="#000",fg=self.green)
        self.chance.place(x=495,y=135)
        self.chr = []
        import string
        p = 200
        i = -1
        yy = 224
        for x in string.ascii_uppercase[:26]:
            i += 1
            self.chr.append(i)
            if i == 13:
                yy += 35
                p = 200
            self.chr[i] = Button(frm,text = x,font = ("verdana",14,"bold"),fg = "#333",bg = "#0BE600",command = lambda idbtn = i:self.check(idbtn))
            self.chr[i].place(x=p,y=yy,width=30,height=30)
            p += 35
        

class start(Frame):
    def __init__(self,frm):
        Frame.__init__(self,frm)
        self.cnvs = cnvs(frm,-1,-1,"./Data/backgrounds/menu.png")
        self.jouer = btn(frm,"Jouer",500,210,("verdana",12,"bold"),"white","#8105FF",lambda: frm.show_frame(playName),150,40)
        self.btnmtxt = StringVar()
        self.btnmtxt.set("Music "+games.musicstate())
        self.music = btn(frm,self.btnmtxt,500,260,("verdana",12,"bold"),"white","#0752FF",lambda : self.edit(),150,40)
        self.quitter = btn(frm,"Quitter",500,310,("verdana",12,"bold"),"white","#FF0018",frm.destroy,150,40)
        self.bsn = lbl(frm,games.bstscore()[0],("verdana",16,"bold"),25,100)
        self.bss = lbl(frm,games.bstscore()[1] if games.bstscore()[1]> 0 else '' ,("verdana",17,"bold"),170,100)
    def edit(self):
        games.music(True)
        self.btnmtxt.set("Music "+games.musicstate())

class win(Frame):
    def history(self):
        with open('data.json') as f:
            data = json.load(f)
        f.close()
        return [data[esm_eli_9a3d_yal3b]["win"],data[esm_eli_9a3d_yal3b]["lose"]]
    def mainmenu(self):
        self.frm.show_frame(start)
    def replay(self):
        games.startGame()
        self.frm.show_frame(engame)
    def __init__(self,frm):
        Frame.__init__(self,frm)
        self.frm = frm
        global score,esm_eli_9a3d_yal3b
        self.cnvs = cnvs(frm,-1,-1,"./Data/backgrounds/playwin.png")
        self.recommencer = btn(frm,'Recommencer',40,295,('times',14,'bold'),'black','#0752FF',lambda : self.replay(),150,50)
        self.main = btn(frm,'Main Menu',500,295,('times',14,'bold'),'black','#FF0018',lambda : self.mainmenu(),150,50)
        self.gagneur = Label(frm,text = 'Bravo '+esm_eli_9a3d_yal3b+' \nVous Avez Gangner Le Partie\nAvec '+str(score)+' Score',font = ('verdana',15,'bold'),fg = '#333',bg = '#fff')
        self.gagneur.place(x=180,y=195)
        self.save()
        self.wins = Label(frm,text = 'Gangner '+str(self.history()[0])+'\nParites',font = ('verdana',13,'bold'),fg = 'green',bg = '#000')
        self.loses = Label(frm,text = 'Perdu '+str(self.history()[1])+'\nParites',font = ('verdana',13,'bold'),fg = 'red',bg = '#000')
        self.wins.place(x=88,y=80)
        self.loses.place(x=470,y=80)
    def save(self):
        global score,esm_eli_9a3d_yal3b,gamestate
        self.win ,self.lose = 0,0
        self.data = self.data()
        self.bestscore = self.data["games"]["best_score"][1]
        if score > self.bestscore:
            self.data["games"]["best_score"] = [esm_eli_9a3d_yal3b,score]
        try:
            self.win = self.data[esm_eli_9a3d_yal3b]["win"]
            self.lose = self.data[esm_eli_9a3d_yal3b]["lose"]
            self.data[esm_eli_9a3d_yal3b]["win"] = self.win+1
        except KeyError:
            self.data[esm_eli_9a3d_yal3b] = {"win":1,"lose":0}
        with open("data.json","w") as f:
            json.dump(self.data,f)
        f.close()

    def data(self):
        with open("data.json") as f:
            data = json.load(f)
        f.close()
        return data

class lose(Frame):
    def history(self):
        with open('data.json') as f:
            data = json.load(f)
        f.close()
        return [data[esm_eli_9a3d_yal3b]["win"],data[esm_eli_9a3d_yal3b]["lose"]]
    def mainmenu(self):
        self.frm.show_frame(start)
    def replay(self):
        games.startGame()
        self.frm.show_frame(engame)
    def __init__(self,frm):
        Frame.__init__(self,frm)
        self.frm = frm
        self.cnvs = cnvs(frm,-1,-1,"./Data/backgrounds/playlose.png")
        self.recommencer = btn(frm,'Recommencer',40,295,('times',14,'bold'),'black','#0752FF',lambda : self.replay(),150,50)
        self.main = btn(frm,'Main Menu',500,295,('times',14,'bold'),'black','#FF0018',lambda : self.mainmenu(),150,50)
        self.save()
        self.loser = Label(frm,text = "D'esole "+esm_eli_9a3d_yal3b+' \nVous Avez Perdu Le Partie',font = ('verdana',15,'bold'),fg = 'red',bg = '#000')
        self.loser.place(x=100,y=80)
        self.wins = Label(frm,text = 'Gangner '+str(self.history()[0])+'\nParites',font = ('verdana',13,'bold'),fg = 'green',bg = '#fff')
        self.loses = Label(frm,text = 'Perdu '+str(self.history()[1])+'\nParites',font = ('verdana',13,'bold'),fg = 'red',bg = '#fff')
        self.wins.place(x=445,y=110)
        self.loses.place(x=455,y=210)
        self.elkelma = Label(frm,text = 'Le Mot est : '+elkelma,font = ('verdana',15,'bold'),fg = 'yellow',bg = '#000')
        self.elkelma.place(x=130,y=250)


    def save(self):
        global score,esm_eli_9a3d_yal3b,gamestate
        self.win ,self.lose = 0,0
        self.data = self.data()
        self.bestscore = self.data["games"]["best_score"][1]
        if score > self.bestscore:
            self.data["games"]["best_score"] = [esm_eli_9a3d_yal3b,score]
        try:
            self.lose = self.data[esm_eli_9a3d_yal3b]["lose"]
            self.data[esm_eli_9a3d_yal3b]["lose"] = self.lose+1
        except KeyError:
            self.data[esm_eli_9a3d_yal3b] = {"win":0,"lose":1}
        with open("data.json","w") as f:
            json.dump(self.data,f)
        f.close()

    def data(self):
        with open("data.json") as f:
            data = json.load(f)
        f.close()
        return data


class jeux(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.show_frame(start)

    def show_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
class games:
    def bstscore():
        with open("data.json") as f:
            data = json.load(f)
        f.close()
        return data["games"]["best_score"]
    def startGame():
        global elkelma,elkelmato_,kelma_,score,chance,findch,t
        t = 40
        elkelma = ''
        elkelmato_ = ''
        kelma_ = ''
        score = 0
        chance = 6
        findch = []
        elkelma = data.tunisie[randint(0,len(data.tunisie)-1)]
        kelma_ = '_ '*len(elkelma)
    def findch(c):
        global kelma_
        kelma_ = ''
        global findch
        i = 0
        for x in elkelma:
            if x.upper() != c.upper():
                i+=1
        if i == len(elkelma):
            pass
        for x in elkelma:
            if c.upper()==x.upper() or x.upper() in findch:
                kelma_ += x + ' '
                if c.upper() not in findch:
                    findch.append(x.upper())
            else:
                kelma_ += '_ '
        if c.upper() in elkelma or c.lower() in elkelma:
            return True
        else:
            return False
        return(rslt)
    def musicstate():
        with open("data.json") as f:
            data = json.load(f)
        f.close()
        return data["games"]["music"]
    def music(change):
        with open("data.json") as f:
            data = json.load(f)
        f.close()
        if change :
            if data["games"]["music"] == "on":
                mixer.music.stop()
                ns = "off"
            elif data["games"]["music"] == "off":
                mixer.music.play(loops=999)
                ns = "on"
            with open("data.json","w") as f:
                data["games"]["music"] = ns
                json.dump(data,f)
            f.close()
        else :
            if data["games"]["music"] == "on":
                mixer.init()
                mixer.music.load("./Data/music/alan_walker_daytime.mp3")
                mixer.music.play(loops=999)
            else : 
                mixer.music.stop()
if __name__ == "__main__":

    app = jeux()
    app.title("Pendu O-<--<")
    app.minsize(665,375)
    app.maxsize(665,375)
    games.music(False)
    app.mainloop()
