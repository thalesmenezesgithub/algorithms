#Função para realizar a pesquisa binária
def search_interative(list, item):
    low = 0
    high = len(list) -1
    
    while low <= high:
        
        #Verifica se e o meio da lista
        mid = round((low + high) / 2)
        guess = list[mid]
        
        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1
            
        else :
            low = mid + 1
            
    return None

my_list = [1, 3, 5, 7 ,9]

print(search_interative(my_list, 3)) 
print(search_interative(my_list, -1)) 