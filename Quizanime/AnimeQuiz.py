import pandas as pd


#CRIAR UMA LISTA
# os numeros no final das perguntas quer dizer que a posiçao do numero é a resposta certa.
perguntas = [["Quem é o protagonista de One Piece?", "Eren Yeager", "Monkey D. Luffy", "Naruto Uzumaki", "Ichigo Kurosaki", 2],
             ["Ichigo, protagonista de Bleach, é...", "Shinigami", "Hollow", "Quincy", "Todos acima", 4],
             ["Em Naruto, quem do time 7 é marcado por orochimaru?", "Kakashi", "Sakura", "Sasuke", "Naruto", 3],
             ["No arco das Quimeras, em Hunter x Hunter, quem o Gon mata?", "Pitou", "Meruem", "Pouf", "Netero", 1],
             ["Qual o nome verdadeiro do Mob, de Mob Psycho 100?", "Roronoa Zoro", "Aizen Sousuke", "Midoriya Izuku", "Shigeo Kageyama", 4],
             ["Stand é o sistema de poder de qual anime?", "Jojo Bizarre Adventure","Kakegurui", "Tokyo Ghoul", "Nanatsu no Taizai", 1],
             ["Em The Promised Neverland, porque existem os 'orfanatos' ?", "Porque sim","Pois as crianças não tem pais", "As crianças são cultivadas como alimentos lá","Porque os orfãos precisam de casas", 3],
             ["No final do manga de Kimetsu no Yaiba, quem vira um demonio?", "Zenitsu", "Inosuke", "Kanao", "Tanjirou", 4]
            ]

# criar dataframe do pandas:
df = pd.DataFrame(perguntas, columns=["Perguntas", "Opção 1", "Opção 2", "Opção 3", "Opção 4", "Resposta"])

# Então vamos salvar em um arquivo excel

df.to_excel("perguntas.xlsx", index=False)

print("Perguntas inseridas com sucesso!")
