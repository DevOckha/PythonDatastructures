class Node:# düğümümüzü oluşrutuyoruz ve düğüm oluştururken data'yı argüman olarak vermek için init fonksiyonunda data parametresini belirtiyoruz
    def __init__(self,data): # 
        self.data = data
        self.next = None # oluşturduğumuz linked list üzerinde her bir düğüm üzerinde dolaşmak için next parametresini None olarak atıyoruz

class LinkedList: # linkedlist'imizi oluşturuyoruz ve parametre olarak linkedlist'imizin baş düğümünü belirtmek için init fonksiyonunda head parametresini çağırıyoruz
    def __init__(self):
        self.head = None

    def print_LL(self):#bağlı listemizi yazdırmak için print_LL methodunu çağıracağız
        if self.head is None:# ilk olarak bağlı listemizin boş olup olmadığını anlamak için head değişkenimizin boş olup olmadığını sorguluyoruz eğer boş ise bağlıliste boş diye ekrana yazdırıyoruz
            print('is empty')
        else:# eğer bağlılistemiz boş değilse else bloğuna giriyoruz
            current = self.head# current adındaki değişkene bağlılistemizin baş elamanını atıyoruz
            while current is not None:# while döngümüzde current değişkenin değeri boş olmadığı sürece while döngüsünün çalışmasını söylüyoruz 
                print(current.data, '--->', end=' ')
                current = current.next# burada ise bağlılistemizin üzerinde gezinmek için bir sonraki değerin referansını current değişkenine atıyoruz döngü boyunca
    
    def add_begin(self, data):#bağlılistemizin başına değer eklemek için add_begin adında bir method tanımlıyoruz ve parametre olarak bir değer alması gerektiğini sölyüyoruz
        node = Node(data)# node adlı değişkene Node sınıfından bir nesne oluşturuyoruz ve  data parametresini Node adlı sınıfa argüman olarak veriyoruz node adlı bir düğümüm oluşturuyoruz
        node.next = self.head# burada ise node değişkenimizin referansıfını bağlılistemizin başında bulunan düğümün referansına atıyoruz
        self.head = node# ve baş düğümümüzü node olarak değiştiriyoruz
            
    def add_end(self, data):#bağlılistemizin sonuna değer eklemek için add_end adında bir method tanımlıyoruz ve parametre olarak bir değer alması gerektiğini sölyüyoruz
        node = Node(data)# node adlı değişkene Node sınıfından bir nesne oluşturuyoruz ve  data parametresini Node adlı sınıfa argüman olarak veriyoruz node adlı bir düğümüm oluşturuyoruz
        if self.head is None:# eğer baş düğümümüz boş ise 
            self.head = node # node değerimizi baş düğüm olarak atıyoruz
        else:# else baş düğümümüz boş değilse else bloğuna giriyoruz
            current = self.head# current adlı değişkene baş düğümüzü atıyoruz
            while current.next is not None:#while döngüsü ile current değerinin referansının boş olmadığı sürece çalışması gerektiğini söylüyoruz
                current = current.next# ve bağlılistemizin üzerinde gezinmek için current adlı değişkene bir sonraki düğümün referansını atıyoruz
            current.next = node # eğer current değişkenin referansı boş ise referans değerine oluşturduğumuz node'un referansını  atıyoruz
     
    def add_after(self, data, x):#burada ise verilen bir değerden sonrasına node eklemek için bir method oluşturuyoruz ve eklemek istediğimiz değeri (data) ve hangi değerden sonra (x) parametrelerini alıyoruz
        current = self.head # current adlı değişkene bağlılistemizin ilk düğümünü atıyoruz
        while current is not None:# current değişkenin boş olmadığı sürece  while ile bağlılistemizin üzerinde geziniyoruz
            if current.data == x: # bağlı listemiz üzerinde gezinirken node değeri x'e eşitse döngüyü kırıyoruz
                break
            else:
                current = current.next# eğer eşit değilse bağlılistemizin üzerinde gezinmeye devam ediyoruz
        if current is None:# eğer current değişkeni None ise istenilen değerin listede olmadığını yazdırıyoruz
            print('node is not present in LL')
        else:# bunlardan hiçbiri değilse ve while döngüsündeki current.data değeri x'e eşitse else bloğuna giriyoruz
            node = Node(data) # node adlı bir düğüm oluşturmak için  Node sınıfından data argümanını alarak bir düğüm oluşturup atıyoruz
            node.next = current.next# ve node düğümünün referansına current değişkeninde data değeri x'e eşit olan düğümün referansına  atıyoruz
            current.next = node # data değeri x'e eşit olan düğümün referansına node adlı düğümü atıyoruz
    
    def add_before(self, data, x):
        if self.head is None:
            print('Linked list is empty!')
            return
        if self.head.data == x:
            node = Node(data)
            node.next = self.head
            self.head = node
            return
        current = self.head
        while current is not None:
            if current.next.data == x:
                break
            current = current.next
        if current.next is None:
            print('Node is not found!')
        else:
            node = Node(data)
            node.next = current.next
            current.next = node

    def insert_empty(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
        else:
            print('Linked list is not empty!')

    def delete_begin(self):
        if self.head is None:
            print('LL is empty')
        else:
            self.head = self.head.next


    def delete_end(self):
        if self.head is None:
            print('LL is empty')
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
    
    def delete_by_value(self, x):
        if self.head is None:
            print("can't delete LL is empty!")
            return 
        if x == self.head.data:
            self.head = self.head.next
            return
        node = self.head
        while node.next is not None:
            if x == node.next.data:
                break
            node = node.next
        if node.next is None:
            print('Node is not present!')
        else:
            node.next = node.next.next

            
            

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.delete_by_value(20)


LL1.print_LL()

