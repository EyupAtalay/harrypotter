import numpy as np


arr = np.array([1, 3, 5, 7, 9])
x = np.searchsorted(arr, 4)
print(x)   # 2





#*****
#arr = np.array([1, 2, 3, 4, 5, 4, 4])
#x = np.where(arr == 4) #4 sayısını arıyor
#print(x) 







#a = np.array([ [4,5,6,7,8],[2,3,4,5,6]])
#b = np.array_split(a, 2,axis=1)
#print(b)



#**
#arr1 = np.array([[1, 2], [3, 4]])
#arr2 = np.array([[5, 6], [7, 8]])

#arr = np.concatenate((arr1, arr2), axis=1)

#print(arr) # iki boyutlu dizi birleştirme




#****
#arr = np.array([1, 2, 3])

#for idx, x in np.ndenumerate(arr): #numaralandırma 
#  print(idx, x)





#***************************************
#a = np.array([[[[2,2,3], [2,3,4],[2,3,66]]]])
#for i in np.nditer(a[:,:2]): #forlar ile birçok döngü yaratıp boyut küçültmek yerine direk içeriği almaya yarıyor.
#    print(i)







#a = np.array([[3,4,5,6,7],[1,2,3,4,5]])
#for i in a[0]:   #direk dizinin ilk boyuttaki tüm verilerini dönderiyoruz.
#    print(i)




#a = np.array([[3242,44,33,22,44],[34,22,44,55,66]])
#for i in a:
#    for x in i:
#        print(x) #2 boyutlu bir dizinin içindeki tüm verilere erişmek






#arr = np.array([[1, 2, 3], [4, 5, 6]])
#newarr = arr.reshape(-1)
#print(newarr)  #dizi boyut küçültüyor





#a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
#b =  a.reshape(4,4) # 4 satır 4 sütün haline dönüştürüyor 
#d = b[0:4:2] # 0:4 parçaları hepsini almaya yarıyor :2 ise 2 li olarak alıyor
#print(d)



#a = np.array([2,3,54,55])
#b = a.view()
#a[0] = 5
#print(b)
#print(a)
#view copy den farkı orjinal dizi de birşeyi değiştiğinde viewde de değişiyor



#a = np.array([2,3,31,22])
#z = a.copy()
#z[0] = 21
#a[0] = 3111
#print(a)
#print(z)


#a = np.array([[2,3,4,5],[2,3,6,7]])
#print(a[1,1:4])



#a = np.array([2,3,5,6])
#print(a[0:4:2])



#b = np.array ([23,4343,44],ndmin=5)
#print(b)
#print(b.ndim)

#a  = np.array([[2,3,4,5],[2,3,4,5]])
#print(a.ndim)