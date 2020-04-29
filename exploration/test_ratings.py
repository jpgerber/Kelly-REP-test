names = {'self.rating_p{}_const{}'.format(i+1, j+1) : ' rating_p{}_const{}'.format(i+1, j+1) for i in range(15) for j in range(15)}
print(names)
for key in names:
    print(key + " =" + names[key])
#names = ['self.rating_p{}_const{} = rating_p{}_const{}'.format(i+1, j+1, i+1, j+1) for i in range(15) for j in range(15)]
#for i in range(len(names)):
#    print(names[i])
