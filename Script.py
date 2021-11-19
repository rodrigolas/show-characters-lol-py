from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
import sqlite3
tabela= sqlite3.connect("database.db")
tabela.execute('''
CREATE TABLE IF NOT EXISTS user(
UserID INTEGER PRIMARY KEY,
usuario VARCHAR(20) NOT NULL,
senha VARCHAR(20) NOT NULL);
''')

class Tela(ScreenManager):
    pass
class Exibicao(App):
    def build(self):
        return Tela()
    def login(self,usuario,senha,lblKiva,ScMain):
        cursor=tabela.cursor()
        find_user= ("SELECT * FROM user WHERE usuario = ? AND senha = ?")
        cursor.execute(find_user,[(usuario.text),(senha.text)])
        results= cursor.fetchall()
        if results:                
            ScMain.current= 'ListaChamps'
        else:
            lblKiva.color= [1,0,0,1]
            lblKiva.text= 'Usuário ou senha inválidos, tente novamente.'    
    
    def registro(self,usuario,senha,lblKivy):        
        username= usuario.text
        password= senha.text
        cursor= tabela.cursor()        
        cursor.execute("SELECT * FROM user WHERE usuario = ?",(username,))
        results = cursor.fetchall()
        if username == '' or password == '':
            lblKivy.color= [1,0,0,1]
            lblKivy.text= 'Insira um nome e uma senha válidas.'
        else:
            if results:
                lblKivy.color= [1,0,0,1]
                lblKivy.text= 'Usuário ja existente, entre com um novo usuário.'    
            else:            
                tabela.execute('INSERT INTO user VALUES(NULL,?,?)',(username,password))
                tabela.commit()
                lblKivy.color=[0,1,0,1]
                lblKivy.text='Registrado com sucesso!'

    def sobre(self,lblSobre,lblSobre1):
        True
        
    def pagChamp(self,txt,lblErro,tela):
        lblErro.text=''
        try:
            tela.current=txt.text
        except:
            lblErro.text='\nNome de campeão inválido, insira um nome que contenha na lista abaixo.\nOBS: Se atente com a letra maiúsula\nEX:Aatrox'
        
Exibicao().run()
