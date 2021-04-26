import matplotlib.pyplot as plt
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun','jul','ago', 'set','out','nov','dez',]
recebidos = [160, 184, 241, 149, 180, 161,132,202,160,139,149,177]
processados = [160, 184, 237, 148, 181, 150,123,156,126,104,124,140]
plt.legend('recebidos')
plt.plot(meses, recebidos,label='Recebidos')
plt.plot(meses,processados,label='Processados')
plt.scatter(meses,recebidos)
plt.scatter(meses,processados)
plt.legend()

plt.xlabel('Meses',fontsize=16)
plt.ylabel('quantidade',fontsize=16)
plt.savefig('grafico.png',dpi=600)
