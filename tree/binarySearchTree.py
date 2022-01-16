#The left subtree of a node contains only nodes with keys lesser tjan node's key.
#The right subtree of a node contains only nodes with keys grater than node's key.
#the left subtree and right subtree each must also be a BST


# 1. Traversing in BST


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

root = BST(10)

list1 = [20, 4, 50 ,4 ,1 ,3 ,5, 6]

for i in list1:
    root.insert(i)
