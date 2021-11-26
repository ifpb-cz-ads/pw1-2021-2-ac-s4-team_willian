#11
mercadoria = int(input('Informe o preço da mercadoria:'));
desconto = int(input('Informe o percentual de desconto: '));
desconto = (mercadoria * (desconto/100));
print('O desconto foi de ', desconto);
mercadoria = (mercadoria - desconto);
print ('O valor final da mercadoria foi de', mercadoria);