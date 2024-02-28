#---------------------------------------------------------------------------
# Tratamento de exceções
# modulos trazem suas proprias exceções 
#---------------------------------------------------------------------------

try:
    print(int("cinquenta")) # gerando uma exceção ValueError 

except Exception: # muito abrangente, idalmente especificar as mais específicas primeiro 
    print("Exceção Exception")
    #pass - continua o programa

except ValueError:
    print("O programa deu uma exceção de ValueError")

except TypeError:
    print("Exceção TypeError") 

else: # opcional
    print("Esse trecho só é executado se o try for bem sucedido.")

finally: 
    print("Este trecho de código sempre será executado no final.")



#---------------------------------------------------------------------------
# Bancos de dados 
#---------------------------------------------------------------------------

