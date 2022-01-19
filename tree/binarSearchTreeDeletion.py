class BST: # BST adından bir class oluşturuyoruz.
    def __init__(self, key):# oluşturduğumuz class çağrılırken key paramteresiyle çağrılması gerektiğini init (yani yapıcı) fonksiyonumuz ile belirtiyoruz
        self.key = key # burada ise oluşturulan nesne üzerinden bir sınıf niteliği olarak çağrılması için key değişkenine atama yapıyoruz
        self.lchild = None # sol altağaç'ı none olarak belirtiyoruz. 
        self.rchild = None # sağ altağaç'ı none olarak belirtiyoruz.

    def insert(self, data): # Binarysearchtree'ye ekleme işlemi yapmak için sınıf insert adında data parametresi alan bir sınıf methodu oluşturuyoruz
        if self.key is None: # root = BST(None) oluşturulan sınıf örneğinin key argümanın boş olup oladığını kontrol ediyoruz 
            self.key = data # eğer boş ise root değerimiz root.insert(20)  insert edilen argümanımız oluyor
            return # return ile işlemi bitiriyoruz
        if self.key == data: # eğer insert ile alınan argüman root değerimize eşitse return ile if işleminden çıkıyoruz
            return
        if self.key > data: # eğer root değerimiz insert ile alınan argümandan küçükse if bloğuna giriyoruz
            if self.lchild: # eğer solaltağacımızda bir değer var ise insert metodunu tekrardan çağırıp solaltağacımızdaki değeri root kabul edip ona göre işlemleri tekrarlıyoruz
                self.lchild.insert(data)
            else:# eğer solaltağacımız False ise else bloğuna giriyoruz ve yeni bir solaltağaç değeri oluşturuyoruz
                self.lchild = BST(data)
        else:# eğer root değerimiz insert ile aldığımız data argümanından küçük ise else bloğuna giriş yapıyoruz
            if self.rchild: # eğer sağaltağacımızda bir değer varsa o değeri sağaltağacın root değeri kabul edip insert işlemine aldığımız değeri tekrardan gönderiyoruz
                self.rchild.insert(data)
            else:# eğer sağaltağacımız boş işe yeni bir sağaltağaç root değeri oluşturuyoruz
                self.rchild = BST(data)



    def search(self, data): # arama işlemi için search adında data parametresi alan bir sınıf methodu tanımladık
        if self.key == data: # eğer aradığımız değer root değerine eşitse node bulundu diye ekrana yazdırıyoruz
            print("Node is Found!")
            return # return ile işlemi bitiriyoruz
        if data < self.key: # eğer aradığımız değer root değerinden küçük ise if bloğuna giriyoruz değilse else
            if self.lchild:# eğer solaltağacımızda bir değer var ise if bloğuna giriyoruz yoksa else
                self.lchild.search(data) # solaltağacımızdaki değeri root olarak alıp üzerinden search işlemini tekrardan çağırıyoruz
            else: # eğer solaltağacımız boş ise node tanımlı değiş yazısını ekrana basıyoruz
                print("Node is not present in tree!")
        else:# eğer data değerimiz root değerimizden büyükse else bloğuna giriyoruz
            if self.rchild:# eğer solaltağacımızda bir değer varsa if bloğuna giriyoruz
                self.rchild.search(data)# ve sağaltağacımızdaki değeri root olarak alıp üzerinden search işlemini tekrardan çağırıyoruz
            else:# eğer sağaltağacımızda değer yoksa node tanımlı değil yazısını yazdırıyoruz.
                print("Node is not present in tree!")


    def preoder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preoder()
        if self.rchild:
            self.rchild.preoder()
            
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key)
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key)


    def delete(self, data, curr):# silmek istenilen değeri parametre olarak alan bir method yazıyoruz

        if self.key is None:# root değerinin boş olup olmadığını kontrol ediyoruz boş ise ağacın boş olduğuğunu yazdırıyoruz
        
            print('Tree is empty!')
        
            return # method'u return ile bitiriyoruz
        
        if data < self.key:# eğer ağacımız boş değilse ve data değeri varsa ve bu değer root değerinden küçük ise bu if bloğuna giriyoruz
        
            if self.lchild:# eğer root'dan  küçük bir değer ise solaltağacımızda bir değer olup olmadığını kontrol ediyoruz. eğer değer varsa bu if bloğuna giriyoruz
        
                self.lchild = self.lchild.delete(data, curr) # burada ise solatlağacımız üzerinden delete fonksiyonu çağırıp solatlağacımız üzerinde dolaşıyoruz 
        
            else:# eğer solaltağacımızda bir değer yoksa silmek istenilen değerin ağacımızda olmadığını yazdırıyoruz
        
                print('Given Node is not present in the tree!')
        
        elif data > self.key:# eğer ağacımız boş değilse ve data değeri varsa ve bu değer root değerinden büyük ise bu if bloğuna giriyoruz
        
            if self.rchild:#eğer root'dan  büyük  bir değer ise sağaltağacımızda bir değer olup olmadığını kontrol ediyoruz. eğer değer varsa bu if bloğuna giriyoruz
        
                self.rchild = self.rchild.delete(data, curr)#burada ise sağatlağacımız üzerinden delete fonksiyonu çağırıp solatlağacımız üzerinde dolaşıyoruz
        
            else:# eğer sağaltağacımızda bir değer yoksa silmek istenilen değerin ağacımızda olmadığını yazdırıyoruz
        
                print('Given Node is not present in the tree!')
                #bundan sonrasını anlamadım anladığım zaman ne anladığımı yazacağım
        
        else:
        
            if self.lchild is None:
        
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
        
                return temp
        
            if self.rchild is None:
        
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
        
                return temp
        
            node = self.rchild
        
            while node.lchild:
        
                node = node.lchild
        
            self.key = node.key 
        
            self.rchild = self.rchild.delete(node.key)
        
        return self


def count(node):
    if node is None:
        return 0 
    return 1 + count(node.lchild) + count(node.rchild)
root = BST(10)

list1 = [1,2]

for i in list1:
    root.insert(i)
print(count(root))
print('Preorder:')    
root.preoder()
if count(root) > 1:

    root.delete(10, root.key)
else:
    print("Can't perform deletion operation!")
print()
print('after deleting:')
root.preoder()