qtd_sistemas = int(input("Quantidade de alunos que cursam Sistemas:"))
qtd_analises = int(input("Quandiade de alunos que cursam Analises:"))
total_alunos = qtd_analises+qtd_sistemas
perc_sistemas = qtd_sistemas/total_alunos*100
perc_analises = qtd_analises/total_alunos*100
print("Total de alunos:", total_alunos) 
print("Total de alunos que cursam Sistemas por cento:", perc_sistemas, "%") 
print("Total de alunos que cursam Analises por cento:", perc_analises, "%") 